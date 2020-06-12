# ShowScraper.py

from bs4 import BeautifulSoup
import requests
import json
from time import sleep

url = 'https://www.themoviedb.org/tv/top-rated'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

showArr = []
for show in content.findAll('div', attrs={"class": "card style_1"}):
    show_url = show.find('a', attrs={"class": "image"})['href'].strip()
    show_response = requests.get('https://www.themoviedb.org' + show_url, timeout=5)
    show_content = BeautifulSoup(show_response.content, "html.parser")

    single_show = show_content.find('div', attrs={"class": "header large border first"})
    genre = single_show.find('span', attrs={"class": "genres"})
    synopsis = single_show.find('div', attrs={"class": "overview"})
    rating = show.find('div', attrs={"class": "outer_ring"})
    certification = single_show.find('span', attrs={"class": "certification"})
    if (certification is not None):
    	certification = certification.text.strip()

    showObject = {
        "title": show.find('a', attrs={"class": "image"})['title'].strip(),
        "synopsis": synopsis.find('p').text.strip(),
        "genre": [g.text.strip() for g in genre.findAll('a')],
        "rating": rating.find('div')['data-percent'].strip(),
        "release_date": show.find('p').text.strip(),
        "duration": single_show.find('span', attrs={"class": "runtime"}).text.strip(),
        "certification": certification
    }

    showArr.append(showObject)

    sleep(5)

with open('../data/topRatedTVShowData.json', 'w') as outfile:
    json.dump(showArr, outfile, indent=4)