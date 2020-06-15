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
<h1 align="center">
  <br>
  README
  <br>
  <br>
</h1>

### DESKRIPSI
Source code berisikan langkah-langkah web scraping dengan cara pengiriman request, parsing HTML, pengambilan data dari HTML, cleaning data, dan pembuatan file json dari data yang didapat.
Data berisikan data-data produk lego untuk usia 12+ dengan atribut berupa nama produk, harga normal, harga sale, rating, dan status

### SPESIFIKASI
Keseluruhan source code menggunakan bahasa pemrograman Phyton, dengan library BeautifulSoup atau bs4 untuk webscraping di bahasa Python, library urllib.request untuk membuka url dan mengirim request, dan library JSON atau json untuk mengubah data ke dalam file json.

Data yang diambil adalah data-data produk lego untuk usia 12+ dari URL https://www.lego.com/en-us/categories/age-12-plus-years dengan mengambil data-data nama produk, harga normal, harga sale, rating, dan status.

Data yang diambil dimasukkan ke dalam file JSON dan diparse menggunakan jsbeautifier.

### HOW TO USE
1. Mengimport library BeautifulSoup
2. URL umum dimasukkan ke dalam variabel `my_url`, untuk kasus ini adalah https://www.lego.com/en-us/categories/age-12-plus-years yang memiliki page total 51 page. `my_url` tersebut ditambahkan string berupa `?page=` dan `i` yang berupa integer untuk menandakan halaman ke berapa. Halaman diiterasi dengan i, dan proses no 3 dilakukan per page.
3. Loop untuk mengirim request ke 51 halaman yang ada dan mengambil `page_html`. Kemudian dilakukan parsing terhadap `page_html` menjadi `page_soup` dan pengambilan container yang berisi data masing-masing product
4. Pembuatan list yang nantinya akan didump ke file json
5. Pemrosesan pembersihan data hanya yang diperlukan dan pemasukan ke dalam list
6. Import library JSON dan list yang sudah ada di dump menjadi file json
7. File JSON dimasukkan ke dalam jsbeautifier sehingga ter-parse dengan baik

### JSON STRUCTURE
```
Product = {
  'name' : str
  'normal_price' : float
  'sale_price' : str
  'rating' : float
  'status' : str
}
```

### SCREENSHOT PROGRAM

![Screenshot 1](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_1.PNG?raw=true "Capture 1")
![Screenshot 2](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_2.PNG?raw=true "Capture 2")
![Screenshot 3](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_3.PNG?raw=true "Capture 3")
![Screenshot 4](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_4.PNG?raw=true "Capture 4")
![Screenshot 5](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_5.PNG?raw=true "Capture 5")
![Screenshot 6](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_6.PNG?raw=true "Capture 6")
![Screenshot 7](/../TUGAS_SELEKSI_1_18218013/screenshots/Capture_7.PNG?raw=true "Capture 7")



### REFERENCE
Berikut adalah beberapa referensi yang digunakan dalam membantu pengerjaan tugas ini :

https://www.youtube.com/watch?v=Ogym0QZLDgw
https://www.youtube.com/watch?v=XQgXKtPSzUI&feature=youtu.be
https://www.youtube.com/watch?v=Ogym0QZLDgw
https://www.youtube.com/watch?v=rnIwmG1AKHg
https://www.petanikode.com/markdown-pemula/
https://beautifier.io/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/


### DEVELOPING
Karena keterbatasan waktu yang dimiliki, author hanya mengambil 5 atribut saja untuk setiap tuple. Sebenarnya bisa ditambahkan atribut lain berupa ketersediaan produk, file gambar, dan diskon yang ada pada produk-produk tertentu serta bisa ditambahkan page yang diproses untuk kategori selain umur 12+ ( 1-2, 3-5, 6-8, 9-11).
Kemudian masih terdapat kesalahan dalam program, yakni ketika menghadapi produk dengan price kosong, sehingga yang tercapture datanya di file json adalah sejumlah 435 produk saja. 

### AUTHOR
Hollyana Puteri Haryono
18218013
Sistem dan Teknologi informasi