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

&nbsp;
### Description

Program dibuat untuk memperoleh data penggunaan internet negara-negara di dunia, data diambil dari 2 buah website yang berbeda

1. Data jumlah pengguna internet dari website https://www.internetworldstats.com/

2. Data kecepatan internet dari website https://www.speedtest.net/global-index

Data dari dua website ini kemudian digabungkan dalam satu buah output file berbentuk JSON. Saya sengaja mengambil data dari dua buah website yang berbeda untuk saling melengkapi, sehingga dapat memberikan lebih banyak insight saat sudah memasuki tahapan visualisasi data nantinya.


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
```
&nbsp;
Keterangan :
```
1. name			: nama negara
2. region		: pembagian wilayah
3. population		: jumlah orang di negara tersebut
4. internetUsers	: jumlah pengguna internet
5. penetration		: persentase pengguna internet di negara tersebut
6. usersInRegion	: persentase pengguna internet dari negara tersebut di region
7. facebookSubs		: jumlah pelanggan facebook
8. speed_data		: data kecepatan internet
	a. broadband_speed	: data kecepatan broadband internet
	b. url			: link ke detail kecepatan internet di negara
	c. mobile_speed		: data kecepatan mobile internet
```

&nbsp;
### Screenshot

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
