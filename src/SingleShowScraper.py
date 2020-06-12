# SingleShowScraper.py

url = 'https://www.themoviedb.org/tv/100-i-am-not-an-animal'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

show = content.find('section', attrs={"class": "header poster no_backdrop"})
genre = show.find('span', attrs={"class": "genres"})
synopsis = show.find('div', attrs={"class": "overview"})
showObject = {
    "certification": show.find('span', attrs={"class": "certification"}).text.strip().encode('utf-8').decode(),
    "genre": [g.text.encode('utf-8').decode() for g in genre.findAll('a')],
    "duration": show.find('span', attrs={"class": "runtime"}).text.strip().encode('utf-8').decode(),
    "synopsis": synopsis.find('p').text.encode('utf-8').decode(),
}
print(showObject)