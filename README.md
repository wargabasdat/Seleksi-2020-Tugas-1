<h1 align="center">
  <br>
  Geekbench Android Benchmark Chart
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Tugas 1 : Data Scraping
  <br>
  <br>
</h2>


## Spesifikasi

### Data Scraping

1. Lakukan _data scraping_ dari sebuah laman web untuk memperoleh data atau informasi tertentu __TANPA MENGGUNAKAN API__. Hasil _data scraping_ ini nantinya akan disimpan dalam DBMS dan digunakan sebagai bahan tugas analisis dan visualisasi data.

2. Daftarkan judul topik yang akan dijadikan bahan _data scraping_ dan DBMS yang akan digunakan pada spreadsheet berikut: [Topik Data Scraping](https://docs.google.com/spreadsheets/d/1TKpyye-ZuoW0npGzylXqvQng3zYm0EzfA9RHjfeFZBk/edit?usp=sharing). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal __8 Juni 2020 pukul 23.59 WIB__

3. Dalam mengerjakan tugas, calon warga basdat terlebih dahulu melakukan _fork_ project github pada link berikut: https://github.com/wargabasdat/Seleksi-2020-Tugas-1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan _pull request_ dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada _repository_ tugas 1, calon warga basdat harus mengumpulkan _file script_, json hasil _data scraping_. _Repository_ terdiri dari _folder_ `src`, `data` dan `screenshots`. _Folder_ `src` berisi _file script_/kode yang __*WELL DOCUMENTED* dan *CLEAN CODE*__, _folder_ `data` berisi _file_ json hasil _scraper_ sedangkan _folder_ `screenshot` berisi tangkapan layar program.

5. Deadline pengumpulan tugas 1 adalah <span style="color:red">__15 Juni 2020 Pukul 23.59 WIB__</span>

6. Sebagai referensi untuk mengenal _data scraping_, asisten menyediakan dokumen "_Short Guidance To Data Scraping_" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance). Mohon memperhatikan etika dalam melakukan _scraping_.

7. Tambahkan juga `.gitignore` pada _file_ atau _folder_ yang tidak perlu di-_upload_, __NB: BINARY TIDAK DIUPLOAD__

8. JSON harus dinormalisasi dan harus di-_preprocessing_
```
Preprocessing contohnya :
- Cleaning
- Parsing
- Transformation
- dan lainnya
```

9. Berikan `README` yang __WELL DOCUMENTED__ dengan cara __override__ _file_ `README.md` ini. `README` harus memuat minimal konten:
```
- Description
- Specification
- How to use
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```
## Description
## Specification
Runtime : Python3
Library : urllib, BeautifulSoup, json 
## How to use
Pada folder src jalankan perintah berikut lewat terminal:
```
python3 scraper.py
```
## JSON Structure
```
[
  {"name": "OnePlus 8",
   "processor": "Qualcomm Snapdragon 865", 
   "clockspeed": 1.8, 
   "score": {"singlecore": 905, 
              "multicore": 3322}
  },
  ...
]
```
## Screenshot program
![alt text](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/tree/master/screenshots/program_1.png)
![alt text](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/tree/master/screenshots/program_2.png)
![alt text](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/tree/master/screenshots/program_3.png)
![alt text](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/tree/master/screenshots/json_data.png)
## Reference
Library yang digunakan:
1. urllib : untuk melakukan request html
2. BeautifulSoup : untuk melakukan parse terhadap laman html
3. json : untuk export hasil ke file .json

## Author
Muhamad Hudan Widzamil <br/>
18218003 <br/>
Sistem dan Teknologi Informasi ITB