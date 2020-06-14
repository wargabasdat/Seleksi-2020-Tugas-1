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
Dalam Tugas 1 Seleksi Warga Basdat 2020 ini, saya membuat sebuah program _data scraping_ pada sebuah web bernama [FIFA Index](https://www.fifaindex.com/players/). Data yang di-_collect_ dari website ini adalah profil pemain sepak bola yang terdaftar dalam permainan __FIFA 20__. Adapun atribut-atribut dari profil tiap pemain tersebut meliputi _overall rating_ __(OVR)__ beserta _rating_ tiap _skill_ yang dimilikinya.

## Spesifikasi
Program ini dibuat dalam bahasa pemrograman Python (3.7.0) dengan menggunakan _libraries_ yang disebutkan dalam bagian __Library Used__ pada __Reference__. Oleh karena itu, untuk program ini hanya dapat dijalankan jika telah ter-_install_ Python 3.7.0 beserta _libraries_ yang digunakan: __pandas__, __bs4__, __re__, __csv__, __requests__, __json__, dan __multiprocessing__.

## How to Use
Sejalan dengan yang diajarkan dalam [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance) agar tidak memberatkan server dengan cara melakukan _request_ dengan tingkat yang wajar, maka proses _scraping_ dilakukan secara serial dengan menjalankan kode program dengan _comment_ __"For peak hours"__. Tetapi, jika traffic dari web tersebut sedang rendah, maka proses scraping dapat dilakukan dengan bantuan _multiprocessing.Pool_ dengan menajalankan kode program dengan _comment_ __"For off-peak hours"__

Untuk perangkat lunak Windows, program webscraper yang nantinya akan membuat _file_ bernama ___FIFA_index_20.csv___ ini dapat dijalankan dengan perintah:
```
transfer_ws.py
```
Dengan syarat telah ter-_install_ library __pandas__, __bs4__, __re__, __csv__, __requests__, __json__, dan __multiprocessing__.

## JSON Structure

Tiap _record_ dalam JSON File hasil proses _data scraping_ ini memiliki atribut-atribut sebagai berikut:

1. __id__: Indeks pemain
2. __name__: Nama pemain
3. __ovr__: _Overall Rating_ pemain
4. __pot__: _Potential Rating_ pemain
5. __nationality__
6. __club__
7. __weak_foot_rating__: _Rating_ dari _weak foot_ pemain dalam skala 1-5
8. __skill_moves_rating__: _Rating_ dari _skill moves_ pemain dalam skala 1-5
9. __club_position"__
10. __height"__
11. __weight__
12. __foot_preference"__
13. __birth_date__
14. __age__
15. __work_rate__
16. __value__: Valuasi pemain terkait dalam mata uang Euro
17. __wage__: Gaji per tahun pemain terkait dalam mata uang Euro
18. __ball_control__
19. __dribbling__
20. __marking__
21. __slide_tackle__
22. __stand_tackle__
23. __aggression__
24. __reactions__
25. __att_position__
26. __interceptions__
27. __vision__
28. __composure__
29. __crossing__
30. __short_pass__
31. __long_pass__
32. __acceleration__
35. __stamina__
34. __strength__
33. __balance__
36. __sprint_speed__
37. __agility__
38. __jumping__
39. __heading__
40. __shot_power__
41. __finishing__
42. __long_shots__
43. __curve__
44. __fk_acc__
45. __penalties__
46. __volleys__
47. __gk_positioning__
48. __gk_diving__
49. __gk_handling__
50. __gk_kicking__
51. __gk_reflexes__

## Screenshot Program

![Screenshot saat Program Dijalankan](https://github.com/fakhrurrida/Seleksi-2020-Tugas-1/blob/master/screenshots/ss_program.PNG?raw=true"SS Program")

![Snippet dari Scraped Data dalam CSV File](https://github.com/fakhrurrida/Seleksi-2020-Tugas-1/blob/master/screenshots/csvFile_snippet.PNG?raw=true "CSV File Snippet")

![Snippet dari Scraped Data dalam JSON File](https://github.com/fakhrurrida/Seleksi-2020-Tugas-1/blob/master/screenshots/jsonFile_snippet.PNG?raw=true "JSONFile Snippet")

## Reference(s)
### Library Used:
__pandas__, __bs4__, __re__, __csv__, __requests__, __json__, dan __multiprocessing__.


## Author

**Fakhrurrida Clarendia Widodo** - *13518091* - [fakhrurrida](https://github.com/fakhrurrida)

