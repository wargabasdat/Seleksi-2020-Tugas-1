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

Description
Pada tugas ini, diambil data top anime dari website https://myanimelist.net/topanime.php
Karena pada page ini ditampilkan 50 judul, maka data yang didapat berjumlah 50
Data scraping dilakukan dengan bahasa python dengan bantuan jupyter notebook

Specification
Data yang diambil mencakup judul anime, nilai rating anime tersebut, jenis anime (serial atau film), dan nomor urut
Semua tipe data yang didapat berupa text

How to use
1. Dengan python, install library beautifulsoup dengan command pip install bs4 pada cmd
2. Mulai menulis kode untuk mengambil url, agar lebih mudah saya menggunakan jupyter notebook
3. Melakukan setting urllib
4. Membuat file .json
5. Mengambil webpage
6. Mengevaluasi webpage, dan mengambil container yang berisi data-data yang diperlukan menggunakan fungsi findAll
7. Melakukan scraping dari container yang didapat untuk memperoleh data yang paling tepat (contoh: nama, score)
8. Menuliskan data yang sudah didapat ke file .json

JSON Structure
{"lists": [{rank,name,score,type}]}

Screenshot
![screenshot1](/screenshots/ss1.png)
![screenshot2](/screenshots/ss2.png)
![screenshot3](/screenshots/ss3.png)

Reference
https://www.youtube.com/watch?v=XQgXKtPSzUI&t=1667s

Author
Vincentius Ian Widi Nugroho 18218034