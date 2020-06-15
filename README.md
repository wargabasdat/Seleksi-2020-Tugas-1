<h1 align="center">
  <br>
  Seleksi Warga Basdat 2020
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Tugas 1 : Data Scraping
  <br>
  <br>
</h2>


## Deskripsi

Data yang saya ambil adalah data dari wesbite toko daring lecia, https://leicacamerausa.com/photography/. Saya menggunakan python dalam melakukan _data scraping_ ini. Saya menggunakan dua fungsi untuk mempermudah. Pertama kali yang saya lakukan adalah mengambil data dan menyimpannya di file csv. Setelah itu, saya ubah dari file csv menjadi json menggunakan library csv dan json.

## Spesifikasi

-urlopen
-BeautifulSoup
-csv
-json
-pandas (ada di-_source code_, namun tidak dipergunakan)

## How to Use

-membuat file csv
-dari website data disimpan di csv
-csv diubah menjadi json

## Json Structure

{
    "20031": {
        "code": "20031",
        " name": "Leica M10-P \"ASC 100 Edition\"",
        " price_without_tax": "$17,500.00",
        " type": "M   Cameras",
        " rating": "0"
    },
    dst.
}

## Screenshot program

![alt text](https://github.com/milmanss/Seleksi-2020-Tugas-1/blob/TUGAS_SELEKSI_1_18218021/screenshot/capture_1.PNG)
![alt text](https://github.com/milmanss/Seleksi-2020-Tugas-1/blob/TUGAS_SELEKSI_1_18218021/screenshot/capture_2.PNG)

## Reference

Library:
-urlopen
-BeautifulSoup
-json
-csv
Referensi web scraping:
-https://www.youtube.com/watch?v=XQgXKtPSzUI&t=320s
-https://medium.com/@hannah15198/convert-csv-to-json-with-python-b8899c722f6d

## Author

Muhamad Ilman Sukarsa - 18218021
