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

## Description
Melakukan data scraping terhadap website iflix.com untuk mendapatkan data video baik Movie, TVSeries, Clip

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
1. Membuka folder src
2. Me-run file "scraper.py" untuk mengekstrak data dari website iflix.com. 
3. Melakukan input nama file bebas yang diakhiri ".json"
4. Berikut merupakan contoh hasil keluaran dari file apabila program berhasil untuk mengekstrak data.
```
Input file name (ex: "data_results.json") : data_results.json
Getting Link....
Getting Link Completed
Extracting 405 of 405 data
399 data succesfully extracted
Data succesfully saved on data_results.json
```
5. File json akan terdapat dalam folder yang sama




## JSON Structure
```
{
	"TVSeries": [ daftar TV series
		{
			"id": id series ,
			"url": link video  ,
			"type": tipe video (TVSeries/Movies/Clip),
			"title": judul video,
			"contentType": kategori konten dari video(Cth: PG-13),
			"year": tahun diterbitkan video ,
			"synopsis": sinopsis video,
			"image": link gambar poster dari video,
			"availabilityStarts": waktu awal film dapat diakses di website,
			"availabilityEnds": waktu akhir film dapat diakses di website,
			"accessCategory": kategori akses (cth: nologinrequired),
			"bestRating": rating terbaik video,
			"ratingCount": jumlah rating video,
			"ratingValue": rata-rata rating video,
			"genre": [ 
				{
					"name": nama genre (cth: Comedy)
				}
			],
			"subtitle": [ daftar subtitle video
				{
					"language": bahasa subtitle (cth: English)
				}
			],
			"starring": [ daftar pemeran video
				{
					"actor": nama aktor (cth: Pevita Pearce)
				}
			],
		        "directors": [ daftar director video
				{
				    "director" : nama director 
				}
		    	],
			"seasons": [ daftar season 
				{
					"name": nama season (cth: Season 1)
					"type": tipe season (TVSeason),
					"dateCreated": tanggal season dimasukkan ke dalam website,
					"numberOfEpisodes": jumlah episode dalam season
				}
			],
			"eligibleRegion": [ daftar negara yang bisa mengakses video ini 
				{
					"country":  nama negara (cth: MY)
				}
			],
			"actionPlatform": [ daftar platform yang bisa mengakses video ini
				{
					"platform": nama platform  (cth : "http://schema.org/AndroidTVPlatform")
				}
			]
		}
	],
	"Movie": [ daftar film
		{
			"id": id film,
			"type": tipe video (TVSeries/Movies/Clip),
			"title": judul film,
			"contentType": kategori konten film (Cth: PG-13),
			"year": tahun keluar film,
			"duration": durasi film,
			"synopsis": sinopsis film,
			"dateCreated": tanggal film dimasukkan ke dalam website,
			"image": link gambar poster film,
			"availabilityStarts": waktu awal film dapat diakses di website,
			"availabilityEnds": waktu akhir film dapat diakses di website,
			"accessCategory": "nologinrequired",
            		"bestRating": rating terbaik film,
			"ratingCount": jumlah rating film,
			"ratingValue": rata-rata rating film,
			"genre": [ daftar genre
				{
					"name": nama genre (Cth : Drama)
				}
			],
			"subtitle": [ daftar subtitle
				{
				    "language" : bahasa subtitle (Cth : English)
				}
            		],
			"starring": [ daftar pemain film
				{
					"actor": nama aktor
				}
			],
			"directors": [ daftar director film
				{
				    "director" : nama director
				}
            		],
			"eligibleRegion": [ daftar negara yang bisa mengakses film ini 
				{
					"country": nama negara (Cth: MY)
				}
			], 
			"actionPlatform": [ daftar platform yang bisa mengakses video ini
				{
					"platform":  nama platform  (cth : "http://schema.org/AndroidTVPlatform")
				}
			]
		}
	],
	"Clip": [ daftar clip
		{
			"id": id clip,
			"type": tipe video (TVSeries/Movies/Clip),
			"description": deskripsi/sinopsis clip,
			"image": link gambar poster clip,
			"title": judul clip
		}
	]
}
```

## Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
1. Screenshot eksekusi program 1
![Image of Eksekusi Program 1](https://github.com/inkariyadi/Seleksi-2020-Tugas-1/blob/master/screenshots/Eksekusi%20Program-1.png)
2. Screenshot eksekusi program 2
3. Screenshot eksekusi program 3
4. Screenshot website iflix.com
5. Screenshot salah satu page Movie dalam iflix.com
6. Screenshot salah satu page TVSeries dalam iflix.com
7. Screenshot salah satu page Clip dalam iflix.com
8. Screenshot file json hasil data scraping


## Reference (Library used, etc)
- By : Inka Anindya Riyadi (13518038)
- Teknik Informatika ITB 2018

- Requirements :
    - Python 3.7.7
    - Library :
        - beautiful soup (install by "pip install bs4")
        - requests
        - json
