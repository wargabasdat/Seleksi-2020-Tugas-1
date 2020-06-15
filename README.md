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
Topik dari data scraping ini adalah data women's clothing dan accesories yang dilakukan dari sebuah laman web yaitu cottonon.com. Tools yang digunakan untuk data scraping ini adalah BeautifulSoup (python).

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

## How to use 
Preresuisites :
- bs4 : pip3 install bs4
- urllib : pip3 install urllib

Langkah-langkah untuk menjalankan program :
- Masuk ke directory "src"
- Jalankan python3 scraping.py pada terminal

## JSON Structure 
Struktur pada file JSON berupa object yang berisi name-value pair, yaitu setiap key memiliki 1 value. Key dari data tersebut terdiri dari Nama, Harga($), KetersediaanWarna, Merek, Promo, dan HargaPromo($). Type untuk nama adalah string, Harga($) adalah float, KetersediaanWarna adalah integer, Merek dan Promo adalah string, lalu untu HargaPromo($) adalah float.

## Screenshot program

![Screenshot1](/screenshots/Screenshot1.png)
![Screenshot2](/screenshots/Screenshot2.png)
![Screenshot3](/screenshots/Screenshot3.png)
![Screenshot4](/screenshots/Screenshot4.png)
![Screenshot5](/screenshots/Screenshot5.png)
![Screenshot6](/screenshots/Screenshot6.png)
![Screenshot7](/screenshots/Screenshot7.png)


## Reference
Library : BeautifulSoup dengan bahasa Python
- https://www.dataquest.io/blog/web-scraping-beautifulsoup/
- https://www.youtube.com/watch?v=XQgXKtPSzUI


## Author 
Nama  : Cynthia Athena M. S.
NIM   : 13518059