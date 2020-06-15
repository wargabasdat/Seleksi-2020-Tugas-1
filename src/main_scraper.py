# Rafael Sean Putra 13518119

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, Executor, wait
import time
import threading
import json
import re

gembok_error = threading.Lock()
gembok_cetak = threading.Lock()
gembok_link = threading.Lock()
gembok_penambah = threading.Lock()
gembok_data = threading.Lock()

executor = ThreadPoolExecutor(50)
pengakses = 0
bulan = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data = []
done = 0
errored = 0


def soup_creator(url):
    global pengakses
    global errored
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
    except:
        msg = "error mengakses " + url
        raise Exception(msg)
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
    global data

    # Membuat BeautifulSoup dari link artikel
    try:
        article_soup = soup_creator(url)
    except Exception as err:
        print(err)
        return;

    # Tanggal kejadian
    date = ''
    if (article_soup.find('div',{'class':'crash-date'})):
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
    else:
        date = 'Data does not exist'

    # Waktu kejadian
    if (article_date[i_date+7] == "a"):
        jam = article_date[i_date+10:i_date+12] + \
            ":" + article_date[i_date+12:i_date+14]
    else:
        jam = 'Data does not exist'

    # Jenis Pesawat dalam Kejadian
    if (article_soup.find('div',{'class':'crash-aircraft'})):
        airplane = article_soup.find("div", {'class': 'crash-aircraft'}).find("div").text
    else:
        airplane = 'Data does not exist'

    # Maskapai/Operator penerbangan pada Kejadian
    if (article_soup.find('div',{'class':'crash-operator'})):
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
    else:
        operator = 'Data does not exist'
    operator = re.sub("-\d","",operator)
    operator = re.sub("_\d","",operator)

    # Fase Penerbangan
    if (article_soup.find('div',{'class':'crash-flight-phase'})):
        phase = article_soup.find('div',{'class':'crash-flight-phase'}).find('div').text
    else:
        phase = 'Data does not exist'
    
    # Terrain kecelakaan
    if (article_soup.find('div',{'class':'crash-site'})):
        terrain = article_soup.find('div',{'class':'crash-site'}).find('div').text
    else:
        terrain = 'Data does not exist'
    phase = re.sub("\((.+)\)","",phase)

    # Jumlah kru, penumpang, dan korban meninggal dunia
    if (article_soup.find('div', {'class': 'crash-crew-on-board'})):
        crew = article_soup.find('div', {'class': 'crash-crew-on-board'}).find('div').text
    else:
        crew = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-crew-fatalities'})):
        crew_death = article_soup.find('div', {'class': 'crash-crew-fatalities'}).find('div').text
    else:
        crew_death = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-pax-on-board'})):
        pax = article_soup.find('div', {'class': 'crash-pax-on-board'}).find('div').text
    else:
        pax = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-pax-fatalities'})):
        pax_death = article_soup.find('div', {'class': 'crash-pax-fatalities'}).find('div').text
    else:
        pax_death = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-other-fatalities'})):
        other_death = article_soup.find('div', {'class': 'crash-other-fatalities'}).find('div').text
    else:
        other_death = 'Data does not exist'

    gembok_data.acquire()
    data.append({
        'Accident Date':date,
        'Accident Time':jam,
        'Airplane Operator':operator,
        'Airplane Type':airplane,
        'Flight Phase':phase,
        'Crash Site Terrain':terrain,
        'Crew on Board':crew,
        'Crew Casualties':crew_death,
        'Passenger on Board':pax,
        'Passenger Casualties':pax_death,
        'Other Casualties':other_death})
    gembok_data.release()

def search_page_iterative(search_url, i):
    # Prosedur search_page_iterative
    # Digunakan untuk membuka setiap laman pencarian dari awal hingga akhir secara rekursif
    # VAR search_url adalah link menuju laman pencarian
    # VAR i menunjukkan indeks laman pencarian ke berapa yang sedang diakses
    url = search_url + str(i)
    try:
        test_soup = soup_creator(url)
    except Exception as err:
        print(err.format())
        return;
    links_container = test_soup.findAll("a", {"class": "red-btn"})
    for link in links_container:
        output = "https://www.baaa-acro.com" + link['href']
        executor.submit(data_scraper, output)


if __name__ == "__main__":
    start_url = "https://www.baaa-acro.com/crash-archives?field_crash_flight_type_target_id=12996&page="
    # t_start = time.perf_counter()
    for i in range(0,1):
        search_page_iterative(start_url, i)
    # executor.submit(data_scraper,'https://www.baaa-acro.com/crash/crash-airbus-a320-214-karachi-97-killed')
    executor.shutdown(wait=True)
    # t_stop = time.perf_counter()
    # print(t_stop - t_start)
    with open('data/data6.json','w') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
