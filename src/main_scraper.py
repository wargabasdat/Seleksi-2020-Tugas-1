# Rafael Sean Putra 13518119

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, Executor, wait
import time
import threading
import psycopg2

gembok_error = threading.Lock()
gembok_cetak = threading.Lock()
gembok_link = threading.Lock()
gembok_penambah = threading.Lock()

executor = ThreadPoolExecutor(50)
pengakses = 0
bulan = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# error_count = 0
# daftar_error = []
conn = None
curs = None

# User scraper1
# pass scrapingnow


def sql_connector():
    global conn
    global curs
    pwd = input("Masukkan pasword akun postgres PostgreSQL: ")
    temp_query = "dbname = postgres user = postgres password=" + pwd
    try:
        temp_conn = psycopg2.connect(temp_query)
    except Exception as err:
        print("error connecting to database postgres")
    temp_conn.autocommit = True
    temp_curs = temp_conn.cursor()
    temp_curs.execute(
        "select exists(SELECT datname FROM pg_catalog.pg_database WHERE datname = 'data_scrap')")
    ada = temp_curs.fetchone()[0]
    if not ada:
        temp_curs.execute("CREATE DATABASE data_scrap")
    temp_curs.close()
    temp_conn.close()
    query = "dbname = data_scrap user = postgres password=" + pwd
    try:
        conn = psycopg2.connect(query)
    except:
        print("error connecting to database data_scrap")
    conn.autocommit = True
    curs = conn.cursor()
    curs.execute(
        "select exists(select * from information_schema.tables where table_name='hasil_scrap')")
    tabel_ada = curs.fetchone()[0]
    if not tabel_ada:
        curs.execute('''CREATE TABLE hasil_scrap(
            Crash_ID SERIAL PRIMARY KEY,
            Operator varchar(100),
            Airplane_Type varchar(100),
            Country varchar (50),
            Crash_Date date,
            Crash_Time time,
            Crew int,
            Crew_Casualties int,
            Pax int,
            Pax_Casualties int,
            Other_Casualties int
        ) ''')


def sql_close():
    curs.close()
    conn.close()


def soup_creator(url):
    # Fungsi soup_creator
    # Digunakan untuk menghasilkan soup dari link yang diberikan
    # VAR url merupakan string berupa link yang akan dibuka dan dibuat soup
    global pengakses
    # global error_count
    # global daftar_error
    while pengakses > 20:
        gembok_link.acquire()
        time.sleep(5)
    gembok_penambah.acquire()
    pengakses += 1
    gembok_penambah.release()
    req = Request(url, headers={
                  'user-agent': 'Windows NT 10.0; Win64; x64; Rafael Sean Putra/13518119@std.stei.itb.ac.id'})
    try:
        url_opened = urlopen(req)
        # print("done link")
    except:
        gembok_error.acquire()
        print("error accessing %s", url)
        gembok_error.release()
        raise Exception("error mengakses link yang diberikan")
    url_read = url_opened.read()
    soup = BeautifulSoup(url_read, 'html.parser')
    url_opened.close()
    gembok_penambah.acquire()
    pengakses -= 1
    gembok_penambah.release()
    if (pengakses <= 20) and (gembok_link.locked()):
        gembok_link.release()
    return soup


def data_scraper(url):
    # Prosedure data_scraper
    # VAR url sebagai link menuju ke laman kecelakaan yang akan diambil informasinya
    # Inisialisasi data yang dibutuhkan
    date = ""
    jam = ""
    operator = ""
    crew = -999
    pax = -999
    crew_death = -999
    pax_death = -999
    other_death = -999

    # Membuat BeautifulSoup dari link artikel
    try:
        article_soup = soup_creator(url)
    except:
        # gembok_error.acquire()
        # # print("error" + url)
        # gembok_error.release()
        return
    # Mencari tanggal kejadian
    article_date = article_soup.find("div", {'class': 'crash-date'}).text
    test = article_date[34:37]
    idx_bulan = 0
    found = False
    while (idx_bulan < 12) and (not found):
        if (test == bulan[idx_bulan]):
            found = True
        else:
            idx_bulan += 1
    if (idx_bulan + 1) < 10:
        date = date + "0" + str(idx_bulan+1)
    else:
        date += str(idx_bulan+1)
    date += "-"
    i_date = 38
    tgl = ""
    while (article_date[i_date] != ","):
        tgl += article_date[i_date]
        i_date += 1
    if len(tgl) == 1:
        date = date + "0" + tgl
    else:
        date += tgl
    date = "-" + date
    date = article_date[i_date+2:i_date+6] + date

    # Mencari waktu kejadian
    if (article_date[i_date+7] == "a"):
        jam = jam + article_date[i_date+10:i_date+12] + \
            ":" + article_date[i_date+12:i_date+14]
    else:
        jam = 'NULL'

    # Mencari jenis pesawat yang mengalami kejadian
    airplane = article_soup.find(
        "div", {'class': 'crash-aircraft'}).find("div").text

    # Mencari maskapai/operator penerbangan dari pesawat yang mengalami kejadian
    article_operator = article_soup.find('div', {'class': 'crash-operator'})
    if (article_operator.find('img')):
        img_operator = article_operator.find('img')['src']
        i_operator = len(img_operator) - 5
        while (img_operator[i_operator] != '/'):
            i_operator -= 1
        operator = img_operator[i_operator+1:len(img_operator)-4]
        operator = operator.replace("%20", " ")
        if (operator[len(operator)-2] == "-"):
            operator = operator[:len(operator)-2]
    else:
        operator = article_operator.find('div').text

    # Mencari negara
    country = article_soup.find(
        'div', {'class': 'crash-country'}).find('div').text
    # print('done country')

    # Mencari jumlah kru, penumpang, dan korban meninggal
    if (article_soup.find('div', {'class': 'crash-crew-on-board'})):
        crew = int(article_soup.find(
            'div', {'class': 'crash-crew-on-board'}).find('div').text)
    crew_death = int(article_soup.find(
        'div', {'class': 'crash-crew-fatalities'}).find('div').text)
    if (article_soup.find('div', {'class': 'crash-pax-on-board'})):
        pax = int(article_soup.find(
            'div', {'class': 'crash-pax-on-board'}).find('div').text)
    pax_death = int(article_soup.find(
        'div', {'class': 'crash-pax-fatalities'}).find('div').text)
    other_death = int(article_soup.find(
        'div', {'class': 'crash-other-fatalities'}).find('div').text)
    # print('done int')

    # Testing, mencetak data
    gembok_cetak.acquire()

    # print('enter')
    try:
        curs.execute("INSERT INTO hasil_scrap (Operator, Airplane_Type, Country, Crash_Date) VALUES (%s, %s,%s,%s)",(operator, airplane, country, date,))
    except Exception as err:
        print(format(err))
    # print('before if')
    curs.execute("SELECT Crash_ID FROM hasil_scrap WHERE Operator = %s and Airplane_Type = %s and Country = %s and Crash_Date = %s", (operator, airplane, country, date,))
    crash_id = curs.fetchone()[0]
    # print(crash_id)
    if (jam != 'NULL'):
        curs.execute("UPDATE hasil_scrap SET Crash_Time=%s WHERE Crash_ID=%s",(jam,crash_id,))
    if (crew != -999):
        curs.execute("UPDATE hasil_scrap SET Crew=%s WHERE Crash_ID=%s",(crew,crash_id,))
    if (crew_death != -999):
        curs.execute("UPDATE hasil_scrap SET Crew_Casualties=%s WHERE Crash_ID=%s",(crew_death,crash_id,))
    if (pax != -999):
        curs.execute("UPDATE hasil_scrap SET Pax=%s WHERE Crash_ID=%s",(pax,crash_id,))
    if (pax_death != -999):
        curs.execute("UPDATE hasil_scrap SET Pax_Casualties=%s WHERE Crash_ID=%s",(pax_death,crash_id,))
    if (other_death != -999):
        curs.execute("UPDATE hasil_scrap SET Other_Casualties=%s WHERE Crash_ID=%s",(other_death,crash_id,)) 
    # print("done input")
    gembok_cetak.release()


def search_page_iterative(search_url, i):
    # Prosedur search_page_iterative
    # Digunakan untuk membuka setiap laman pencarian dari awal hingga akhir secara rekursif
    # VAR search_url adalah link menuju laman pencarian
    # VAR i menunjukkan indeks laman pencarian ke berapa yang sedang diakses
    url = search_url + str(i)
    try:
        test_soup = soup_creator(url)
    except:
        # print("error accesing %s",url)
        return
    links_container = test_soup.findAll("a", {"class": "red-btn"})
    for link in links_container:
        output = "https://www.baaa-acro.com" + link['href']
        executor.submit(data_scraper, output)


if __name__ == "__main__":
    sql_connector()
    start_url = "https://www.baaa-acro.com/crash-archives?field_crash_flight_type_target_id=12996&page="
    for i in range(0, 62):
        search_page_iterative(start_url, i)
    # executor.submit(data_scraper, "https://www.baaa-acro.com/crash/crash-boeing-737-524-usinsk")
    # executor.submit(data_scraper, "https://www.baaa-acro.com/crash/crash-piper-pa-31t-cheyenne-near-eatonton-5-killed")
    # executor.submit(data_scraper, "https://www.baaa-acro.com/crash/crash-farman-f60-goliath-belgium")
    # executor.submit(data_scraper, "https://www.baaa-acro.com/crash/ground-fire-airbus-a330-343-beijing")
    # executor.submit(data_scraper, "https://www.baaa-acro.com/crash/crash-britten-norman-bn-2b-27-islander-puerto-montt-6-killed")
    # executor.submit(data_scraper, "https://www.baaa-acro.com/crash/crash-cessna-208b-grand-caravan-near-tastiota-2-killed")
    executor.shutdown(wait=True)
    # print("Total data error= " + str(error_count))
    # if error_count > 0:
    #     for error in daftar_error:
    #         print("error link: %s", error)
    sql_close()
