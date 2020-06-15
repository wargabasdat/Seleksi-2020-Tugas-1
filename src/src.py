from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# mengambil url
page_url = "https://myanimelist.net/topanime.php"

# membuka koneksi dan download html page dari url
uClient = uReq(page_url)

# parse html menjadi soup data structure
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# mengambil semua data dari page
containers = page_soup.findAll("tr", {"class": "ranking-list"})

# menentukan nama file yang ingin ditulis
out_filename = "hasil.json"

# membuka file dan menulis beberapa teks ke file
f = open(out_filename, "w")
f.write("{ \n \"lists\": [")

# set variabel untuk digunakan pada looping
count=1

# looping untuk semua data yang didapat di page
for container in containers:
    # mengambil nomor urut ranking dengan mengambil text dari tag td.span
    rank = container.td.span.text

    # mengambil judul dengan mencari tag td yang sesuai
    # kemudian mencari div yang sesuai dari td
    # kemudian mengambil text dari tag a
    td2 = container.findAll("td", {"class": "title al va-t word-break"})
    td2div = td2[0].div.findAll("div", {"class": "di-ib clearfix"})
    name = td2div[0].a.text

    # mengambil nilai dengan mencari tag td yang memiliki class score ac fs14
    # kemudian mengambil text pada tag div.span
    tdt = container.findAll("td", {"class": "score ac fs14"})
    score = tdt[0].div.span.text

    # mengambil jenis dengan mencari div yang sesuai
    # kemudian mengambil 3 baris teks dan mengambil baris pertama saja
    # dan melakukan strip untuk merapikan text yang didapat
    td2info = td2[0].div.findAll("div", {"class": "information di-ib mt4"})
    jenis = td2info[0].text.split('\n')[1].strip()

    # menulis data yang sudah didapat ke file dengan format json
    f.write("{\n\"rank\": \"" + rank + "\",\n")
    f.write("\"name\": \"" + name + "\",\n")
    f.write("\"score\": \"" + score + "\",\n")
    f.write("\"type\": \"" + jenis + "\"\n}")
    if (count != len(containers)):
        f.write(",")
    count+=1
    
f.write("\n]\n}")

# menutup file
f.close()