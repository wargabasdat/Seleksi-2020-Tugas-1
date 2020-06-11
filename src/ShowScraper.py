# ShowScraper.py

from bs4 import BeautifulSoup
import requests
import json


url = 'https://www.themoviedb.org/tv/top-rated'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

showArr = []
for show in content.findAll('div', attrs={"class": "card style_1"}):
    rating_ring = show.find('div', attrs={"class": "outer_ring"})
    showObject = {
        "title": show.find('a', attrs={"class": "image"})['title'].encode('utf-8').decode(),
        "site": show.find('a', attrs={"class": "image"})['href'].encode('utf-8').decode(),
        "picture": show.find('img', attrs={"class": "poster lazyload lazyloaded"})['alt src'].encode('utf-8').decode(),
        "rating": rating_ring.find('div')['data-percent'].encode('utf-8').decode(),
        "released_date": show.find('p').text.encode('utf-8').decode()
    }
    showArr.append(showObject)

with open('../data/topRatedTVShowData.json', 'w') as outfile:
    json.dump(showArr, outfile)