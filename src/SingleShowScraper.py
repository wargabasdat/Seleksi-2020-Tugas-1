# SingleShowScraper.py

from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.themoviedb.org/tv/100-i-am-not-an-animal'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

show = content.find('section', attrs={"class": "header poster no_backdrop"})
genre = show.find('span', attrs={"class": "genres"})
synopsis = show.find('div', attrs={"class": "overview"})
showObject = {
    "certification": show.find('span', attrs={"class": "certification"}).text.strip(),
    "genre": [g.text.strip() for g in genre.findAll('a')],
    "duration": show.find('span', attrs={"class": "runtime"}).text.strip(),
    "synopsis": synopsis.find('p').text.strip(),
}
print(showObject)