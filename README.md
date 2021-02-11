<h1 align="center">
  <br>
  Seleksi Warga Basdat 2020
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Tugas 1: Data Scraping
  <br>
  <br>
</h2>

## Deskripsi
Program ini adalah sebuah *web scraper* dalam bahasa Python untuk mengambil data resep makanan manis dari [allrecipes.com]. Data yang diambil meliputi nama dan penulis resep, kategori, *rating*, waktu memasak, jumlah bahan, dan informasi nutrisi. Dicantumkan pula ID resep sehingga halaman resep yang asli dapat diakses melalui tautan ```allrecipes.com/<id resep>```.

Data hasil *scraping* diharapkan dapat menjadi alat bantu untuk membandingkan berbagai versi resep dan menentukan resep terbaik untuk dimasak sekarang berdasarkan waktu luang, pola diet, dan budget yang dimiliki (dengan asumsi semakin sedikit bahannya, semakin terjangkau harganya).

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

## Cara Menggunakan
1. *Clone repository* ini
2. Buka cmd atau terminal pada direktori ```\src```
3. Jalankan perintah ```py scraper.py``` atay ```python scraper.py```

## Struktur JSON
```
{
    "id": "/recipe/12101/",
    "dessert-type": "Pies",
    "name": "Grandma's Butterscotch Pie",
    "author": "dschecht",
        "rating": {
            "stars": 4.28,
            "rated-by": 118
        },
        "time": {
            "prep": "25 mins",
            "cook": "35 mins",
            "total": "1 hr"
        },
        "ingredients-count": 8,
        "nutritions-per-serving": {
            "calories-in-cal": 259,
            "total-fat-in-gr": 8.9,
            "cholesterol-in-mg": 60.0,
            "sodium-in-mg": 293.0,s
            "carb-in-gr": 41.5,
            "protein-in-gr": 3.4
        }
}
```

## Screenshot
![Image of Code](https://github.com/anindyy/Seleksi-2020-Tugas-1/blob/master/screenshots/code.jpg?raw=true)

## Referensi
### Library
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [re](https://docs.python.org/3/library/re.html)
- [time](https://docs.python.org/3/library/time.html)

### Bacaan
- [Data Scraping Guidance](bit.ly/DataScrapingGuidance)
- [Web Scraping Tutorial](https://www.dataquest.io/blog/web-scraping-beautifulsoup/)
- [Guide to robots.txt](https://varvy.com/robottxt.html)

<h4 align="center">
  <br>
  Anindya Prameswari / 135 18 034
</h4>