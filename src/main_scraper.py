# Rafael Sean Putra 13518119

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait
import time
import threading
import json
import re

gembok_soup = threading.Lock()
gembok_pengakses = threading.Lock()
gembok_data = threading.Lock()

executor = ThreadPoolExecutor(50)

bulan = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data = []

data_amount = 0
pengakses = 0


def soup_creator(url):
    # Membuka link yang diterima dan membuat soup menggunakan BeautifulSoup dari link tersebut
    global pengakses
    while pengakses > 20:
        gembok_soup.acquire()
        time.sleep(5)
    gembok_pengakses.acquire()
    pengakses += 1
    gembok_pengakses.release()
    req = Request(url, headers={
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0; Rafael Sean Putra/13518119@std.stei.itb.ac.id'})
    try:
        url_opened = urlopen(req)
    except:
        msg = "error mengakses " + url
        raise Exception(msg)
    url_read = url_opened.read()
    soup = BeautifulSoup(url_read, 'html.parser')
    url_opened.close()
    gembok_pengakses.acquire()
    pengakses -= 1
    gembok_pengakses.release()
    if (pengakses <= 20) and (gembok_soup.locked()):
        gembok_soup.release()
    return soup

def last_page_finder(url):
    #Mencari halaman terakhir dari search page yang dibuka
    try:
        first_soup = soup_creator(url)
    except Exception as err:
        print(err)
        return
    if (first_soup.find('li',{'class':'pager__item pager__item--last'})):
        last_button = first_soup.find('li',{'class':'pager__item pager__item--last'})
        last_link = last_button.find('a')['href']
        j = len(last_link) - 1
        last = ""
        while (last_link[j] != '='):
            last = last_link[j] + last
            j -= 1
        last_page = int(last)
    else:
        last_page = 0
    return last_page

def data_scraper(url):
    global data
    global data_amount
    # Membuat BeautifulSoup dari link artikel
    try:
        article_soup = soup_creator(url)
    except Exception as err:
        print(err)
        return

    # Tanggal kejadian
    if (article_soup.find('div', {'class': 'crash-date'})):
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
            date = "0" + str(idx_bulan+1)
        else:
            date = str(idx_bulan+1)
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

    # Jenis Pesawat dalam Kejadian
    if (article_soup.find('div', {'class': 'crash-aircraft'})):
        airplane = article_soup.find(
            "div", {'class': 'crash-aircraft'}).find("div").text
        if airplane == "Unknown":
            airplane = 'Data does not exist'
    else:
        airplane = 'Data does not exist'

    # Maskapai/Operator penerbangan pada Kejadian
    if (article_soup.find('div', {'class': 'crash-operator'})):
        article_operator = article_soup.find(
            'div', {'class': 'crash-operator'})
        if (article_operator.find('img')):
            link_operator = article_operator.find('a')['href']
            link_operator = re.sub(
                ".+field_crash_operator_target_id=", "", link_operator)
            operator = re.sub(" \(\d+\)", "", link_operator)
        else:
            operator = article_operator.find('div').text
    else:
        operator = 'Data does not exist'
    operator = re.sub("%26","&",operator)

    # Lokasi Kecelakaan
    if (article_soup.find('div', {'class': 'crash-country'})):
        if (article_soup.find('div', {'class': 'crash-country'}).find('div').text == 'World'):
            location = article_soup.find(
                'div', {'class': 'crash-location'}).find('div').text
        else:
            location = article_soup.find(
                'div', {'class': 'crash-country'}).find('div').text
            if (article_soup.find('div', {'class': 'crash-location'})):
                daftar_lokasi = article_soup.find(
                    'div', {'class': 'crash-location'}).findAll('div')
                if (re.search("All ", daftar_lokasi[1].text)):
                    location_2 = daftar_lokasi[0].text
                else:
                    location_2 = daftar_lokasi[1].text
                if (location_2 != location):
                    location = location_2 + ", " + location
        location = re.sub(" \(.+\)", "", location)
    else:
        location = 'Data does not exist'

    # Fase Penerbangan
    if (article_soup.find('div', {'class': 'crash-flight-phase'})):
        phase = article_soup.find(
            'div', {'class': 'crash-flight-phase'}).find('div').text
    else:
        phase = 'Data does not exist'
    phase = re.sub(" \((.+)\)", "", phase)

    # Jumlah kru, penumpang, dan korban meninggal dunia
    if (article_soup.find('div', {'class': 'crash-crew-on-board'})):
        if (article_soup.find('div', {'class': 'crash-crew-on-board'}).find('div').text == '0'):
            crew = 'Data does not exist'
        else:
            crew = article_soup.find(
                'div', {'class': 'crash-crew-on-board'}).find('div').text
    else:
        crew = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-crew-fatalities'})):
        crew_death = article_soup.find(
            'div', {'class': 'crash-crew-fatalities'}).find('div').text
    else:
        crew_death = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-pax-on-board'})):
        if (crew == 'Data does not exist') and (article_soup.find('div', {'class': 'crash-pax-on-board'}).find('div').text == '0'):
            pax = 'Data does not exist'
        else:
            pax = article_soup.find(
                'div', {'class': 'crash-pax-on-board'}).find('div').text
    else:
        pax = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-pax-fatalities'})):
        pax_death = article_soup.find(
            'div', {'class': 'crash-pax-fatalities'}).find('div').text
    else:
        pax_death = 'Data does not exist'
    if (article_soup.find('div', {'class': 'crash-other-fatalities'})):
        other_death = article_soup.find(
            'div', {'class': 'crash-other-fatalities'}).find('div').text
    else:
        other_death = 'Data does not exist'

    # Menambahkan semua data
    gembok_data.acquire()
    data.append({
        'Accident Date': date,
        'Airplane Operator': operator,
        'Airplane Type': airplane,
        'Flight Phase': phase,
        'Crash Location': location,
        'Crew on Board': crew,
        'Crew Casualties': crew_death,
        'Passenger on Board': pax,
        'Passenger Casualties': pax_death,
        'Other Casualties': other_death})
    data_amount += 1
    gembok_data.release()


def search_page_iterative(search_url, i):
    # Membuka laman pencarian dan mengakses semua artikel kejadian yang terdapat pada laman pencarian
    url = search_url + str(i)
    try:
        test_soup = soup_creator(url)
    except Exception as err:
        print(err.format())
        return
    links_container = test_soup.findAll("a", {"class": "red-btn"})
    for link in links_container:
        output = "https://www.baaa-acro.com" + link['href']
        executor.submit(data_scraper, output)


if __name__ == "__main__":
    nama_file = input("Silahkan masukkan nama file (tanpa extensi .json): ")
    start_url = "https://www.baaa-acro.com/crash-archives?field_crash_flight_type_target_id=12996&page="
    j = last_page_finder(start_url+"0")
    for i in range(0, j+1):
        search_page_iterative(start_url, i)
    executor.shutdown(wait=True)
    direktori = 'data/' + nama_file + '.json'
    with open(direktori, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(str(data_amount) + " data berhasil disimpan di " + direktori)
