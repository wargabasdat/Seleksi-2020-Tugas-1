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
  Status Internet di Dunia
  <br>
  Muhammad Fauzan Al-Ghifari
  <br>
  13518112
  <br>
  <br>
</h2>

### Update!!!
Menambahkan web ketiga untuk mengambil data gross national income per capita

&nbsp;
### Description

Program dibuat untuk memperoleh data penggunaan internet negara-negara di dunia, data diambil dari 3 buah website yang berbeda

1. Data jumlah pengguna internet dari website https://www.internetworldstats.com/

2. Data kecepatan internet dari website https://www.speedtest.net/global-index

3. Data gross national income per capita dari website https://en.m.wikipedia.org/wiki/List_of_countries_by_GNI_(nominal)_per_capita

Data dari dua website ini kemudian digabungkan dalam satu buah output file berbentuk JSON. Saya sengaja mengambil data dari dua buah website yang berbeda untuk saling melengkapi, sehingga dapat memberikan lebih banyak insight saat sudah memasuki tahapan visualisasi data nantinya.

### Demo Video
Link : https://www.youtube.com/watch?v=NbUMcPp-5L4&t=5s

<a href = "https://www.youtube.com/watch?v=NbUMcPp-5L4&t=5s">
<img src="/screenshots/Screenshot (116).jpg" href="https://www.youtube.com/watch?v=NbUMcPp-5L4&t=5s" target="blank" alt="Video" width="350"/>
<a/>

&nbsp;
### Spesification

Program ini menggunakan JavaScript dengan library Puppeteer. Pastikan komputer anda sudah terinstall ___Node.JS___

Node.js dapat diunduh pada situs https://nodejs.org/en/download/


&nbsp;
### How to Use

1. Download atau clone repository ini

2. Buka folder folder src

3. Jalankan terminal/node.js di folder src

4. Jalankan command berikut pada terminal untuk menginstall library yang dibutuhkan
```
npm install
```
5. Jalankan command berikut pada terminal untuk menjalankan program
```
node index.js
```
6. Tunggu hingga proses scraping selesai

7. Data output akan tersimpan pada folder data dengan nama __data.JSON__


&nbsp;
### JSON Structure
Berikut adalah contoh salah satu struktur data hasil scraping
```
 {
      "name": "Afghanistan",
      "region": "Asia",
      "population": 38928346,
      "internetUsers": 7337489,
      "penetration": 18.8,
      "usersInRegion": 0.3,
      "facebookSubs": 3848400,
      "speed_data": {
         "broadband_speed": 6.95,
         "url": "https://www.speedtest.net/global-index/afghanistan#fixed",
         "mobile_speed": 6.02
      }
      "GNI": 540
}
```
&nbsp;
Keterangan :
```
1. name			: nama negara
2. region		: pembagian wilayah
3. population		: jumlah orang di negara tersebut
4. internet_users	: jumlah pengguna internet
5. penetration		: persentase pengguna internet di negara tersebut
6. users_region		: persentase pengguna internet dari negara tersebut di region
7. facebook_subs	: jumlah pelanggan facebook
8. speed_data		: data kecepatan internet
	a. broadband_speed	: data kecepatan broadband internet
	b. url			: link ke detail kecepatan internet di negara
	c. mobile_speed		: data kecepatan mobile internet
9. GNI			: gross national income
```

&nbsp;
### Screenshot

isi index.js

<img src="/screenshots/Capture1.PNG" alt="Capture1" width="800"/>
<img src="/screenshots/Capture2.PNG" alt="Capture2" width="800"/>
<img src="/screenshots/Capture3.PNG" alt="Capture3" width="800"/>
<img src="/screenshots/Capture4.PNG" alt="Capture4" width="800"/>


&nbsp;
### Reference
* puppeteer : untuk melakukan scraping
* fs : untuk menuliskan hasil ke file JSON

&nbsp;
### Author
```
Muhammad Fauzan Al-Ghifari
13518112
```
