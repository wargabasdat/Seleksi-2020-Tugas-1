<h2>
  <br>
  Aircraft Accident Archives Data Scraper
  <br>
</h2>

## Description

Program ini digunakan untuk melakukan <i> data scraping </i> data tentang kecelakaan penerbangan pesawat komersial dari website milik [Bureau of Aircraft Accidents Archives](https://baaa-acro.com).

Hasil dari <i>data scraping</i> yang dilakukan oleh program adalah beberapa komponen dari kecelakaan penerbangan pesawat komersil, yaitu sebagai berikut:
- Tanggal dan waktu kejadian
- Jenis pesawat yang mengalami kejadian
- Maskapai/ Operator penanggung jawab kejadian
- Fase penerbangan saat kejadian terjadi
- Lokasi dan topografi daerah tempat kejadian terjadi
- Jumlah kru dan penumpang pada pesawat
- Jumlah korban meninggal dunia


## Spesification

Runtime: Python ver. 3.7.7

Library:
- BeautifulSoup (bs4)
- concurrent.futures
- json
- re
- Request
- threading

## How to Use

1. Masukkan script berikut ke dalam CLI pada <i>root directory</i> (*Note : Bila kode tidak berjalan, silahkan coba lagi dengan mengganti "python" dengan "py" atau "python3")
```
$ python src/main_scraper.py
```
2. Masukkan nama file hasil <i>data scraping</i> yang diinginkan tanpa ekstensi .json
3. Tunggu beberapa saat
4. Akan muncul teks yang menandakan proses <i>data scraping</i> telah selesai
5. Hasil <i>data scraping</i> dapat dilihat di folder data

## JSON Structure

```
[
    {
      "Accident Date": "2019-09-16",
      "Airplane Operator": "twoFlex",
      "Airplane Type": "Cessna 208B Grand Caravan",
      "Flight Phase": "Takeoff ",
      "Crash Location": "Amazonas, Brazil",
      "Crew on Board": "2",
      "Crew Casualties": "0",
      "Passenger on Board": "8",
      "Passenger Casualties": "0",
      "Other Casualties": "0"
    },
    {
    ...
    },
    ...
]
```

## Screenshot Program

![alt](/screenshots/ss-script1.jpg "Snippet 1 dari script")
![alt](/screenshots/ss-script2.jpg "Snippet 2 dari script")
![alt](/screenshots/ss1.jpg "Program dijalankan menggunakan Command Prompt")
![alt](/screenshots/hasil.jpg "Bagian dari file Json hasil data scraping")
## References

Library yang digunakann:
- [bs4](https://www.crummy.com/software/BeautifulSoup/)
- [concurrent futures](https://docs.python.org/3/library/concurrent.futures.html)
- [json](https://docs.python.org/3/library/json.html)
- [re](https://docs.python.org/3/library/re.html)
- [request](https://docs.python.org/3/library/urllib.request.html)
- [threading](https://docs.python.org/3/library/threading.html)

<h5>Rafael Sean Putra 13518119</h5>
