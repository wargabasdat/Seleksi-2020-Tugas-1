<h1 align="center">
  <br>
  Geekbench Android Benchmark Chart
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

## Description
Mengoleksi data hasil benchmark ponsel android yang di-_list_ secara resmi oleh Geekbench. _Data scraping_ dilakukan terhadap laman [berikut](https://browser.geekbench.com/android-benchmarks/). Hasil koleksi data mencakup data nama perangkat, _System On Chip_ yang digunakan, _clock speed_ (dalam Ghz), dan hasil _benchmark_ baik _single core_ dan _multicore_.
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
![1](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/blob/master/screenshots/program_1.png)
![2](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/blob/master/screenshots/program_2.png)
![3](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/blob/master/screenshots/program_3.png)
![4](https://github.com/hudanwidzamil/Seleksi-2020-Tugas-1/blob/master/screenshots/json_data.png)
## Reference
Library yang digunakan:
1. urllib : untuk melakukan request html
2. BeautifulSoup : untuk melakukan parse terhadap laman html
3. json : untuk export hasil ke file .json

## Author
Muhamad Hudan Widzamil <br/>
18218003 <br/>
Sistem dan Teknologi Informasi ITB