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

__Description__

Data scraping koleksi wanita dari web https://www.zara.com/id/en/

__Specification__
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

__How to use__
- masuk ke direktori penyimpanan folder
- masuk kedalam folder src
- how to run : python3 basdat.py
- lihat data hasil scraping pada file zara_women.json pada folder data

p.s. dibutuhkan waktu sekitar 3 menit hingga program selesai bekerja, jika ingin melihat url page yang sedang di-scrape pada setiap waktu, silahkan membuka command pada baris 113

__JSON Structure__

Setiap tuple data berisikan :
1. ID
2. Kode Produk
3. Nama produk
4. Label Produk (menyatakan apakah barang new / special price (beserta persentasenya jika merupakan barang sale) / limited edition , jika tidak terdapat label akan bernilai "None")
5. Kategori Produk
6. Subkategori Produk (contoh: untuk kategori dress terdapat Subkategori mini, midi dan maxi, jika barang tidak memiliki subkategori maka akan bernilai "None")
7. Harga Awal / Asli produk
8. Harga Diskon produk (Jika bukan barang sale, maka Harga Diskon -1)

__Screenshot program__

Screenshot 1
![Screenshot1](/screenshots/ss1.png)

Screenshot 2
![Screenshot2](/screenshots/ss2.png)

Screenshot 3
![Screenshot3](/screenshots/ss3.png)

Screenshot 4
![Screenshot4](/screenshots/ss4.png)

Screenshot 5
![Screenshot5](/screenshots/ss5.png)


__Reference__

Library yang digunakan :

1. json untuk menghasilkan file json
2. BeautifulSoup4 untuk html parser
3. urllib.request untuk mendapatkan script HTML dari url
4. pymongo untuk menghubungkan dengan cloud database Atlas

__Author__

Chandrika Azharyanti
13518001
