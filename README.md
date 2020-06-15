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
  Data Tanaman Hias dari Crocus
  <br>
</h2>

## Description

_Web scraper_ untuk mengambil data tanaman dari crocus.co.uk berupa:

- Nama tanaman
- Jenis pot yang dibutuhkan
- Harga tanaman
- Ketersediaan tanaman
- Rating tanaman (jika ada)
- Posisi cocok untuk tanaman

## Spesifikasi

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

## How To Use
Clone repository ini, lalu jalankan perintah berikut pada repository ini
```
cd src
py scrapper.py
```

Hasil _scrapping_ dapat dilihat pada file plants.json di directory data.

## JSON Structure
```
{
  "plants": [
    {
      "name": "Polystichum aculeatum",
      "prop": "2 litre pot",
      "price": 16.99,
      "availability": "within 4 weeks",
      "rating": {
        "avg-rating": 5,
        "rating-count": 3
      },
      "position": [
        "full",
        "partial shade"
      ],
      "nickname": "hard shield fern"
    },
    ...
```
#### Keterangan
- __name__ - nama (latin) tanaman
- __prop__ - pot sesuai dengan tanaman
- __price__ - harga tanaman
- __availability__ - ketersediaan tanaman
- __rating__ - rating tanaman
  - __avg-rating__ - rata-rata rating
  - __rating-count__ - jumlah orang yang meninggalkan rating
- __position__ - posisi ideal tanaman untuk tumbuh
- __nickname__ - nama (umum) tanaman


## Screenshot Program

![ss](screenshots/code.PNG)

## References
1. __Python__
2. __BeautifulSoup__ - Kakas untuk melakukan parsing HTML 
3. __requests__ - Kakas untuk melakukan request pada URL yang diinginkan
4. __json__ - Kakas untuk menyimpan data dalam format .json
5. __time__ - Kakas untuk memberikan jeda waktu pada setiap requests

## Author
__William Fu__ - 13518055