# ShowScraper.py

# Indra Febrio Nugroho
# 13518016
# indrafbrngrh@gmail.com
# Data Source: themoviedb.org

# import libraries
from bs4 import BeautifulSoup
import requests
import json
from time import sleep
import calendar

def strToDate(string):
    # string is always in a format "[MMM] [DD], [YYYY]"
    # where M is month, D is date, and Y is year
    year = string[8:13]
    date = string[4:6]
    month = string[0:3]
    # convert abbreviated month name to month number
    month_dict = {v: k for k,v in enumerate(calendar.month_abbr)}
    month = month_dict[month]
    
    # rewrite website date format into a common date format
    return (str(year) + '-' + str(month) + '-' + str(date))

def getShowDetails(show_url):
    # scrape tv show details
    # from the list of top rated tv show
    # shown on the website
    global header
    global url
    response = requests.get(url + show_url, headers=header, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')
    container = soup.find('div', attrs={'class': 'header large border first'})

    show = {}
    show['synopsis'] = (container.find('div', attrs={'class': 'overview'})).find('p').text.strip()
    show['genre'] = [genre.text.strip() for genre in (container.find('span', attrs={'class': 'genres'})).findAll('a')]
    try:
        show['duration'] = container.find('span', attrs={'class': 'runtime'}).text.strip()
    except AttributeError:
        show['duration'] = None
    
    try:
        show['certification'] = (container.find('span', attrs={'class': 'certification'})).text.strip()
    except AttributeError:
        show['certification'] = None

    return show

def getData(soup):
    # scrape the list of top rated tv shows
    show_array = []

    for container in soup.findAll('div', attrs={'class': 'card style_1'}):
        show_url = container.find('a', attrs={'class': 'image'})['href'].strip()
        show_details = getShowDetails(show_url)

        show = {}
        show['title'] = container.find('a', attrs={'class': 'image'})['title'].strip()
        show = {**show, **show_details}
        show['release_date'] = strToDate((container.find('p')).text.strip())
        show['rating'] = float((container.find('div', attrs={'class': 'outer_ring'})).find('div')['data-percent'].strip())

        show_array.append(show)

        sleep(2)

    return show_array

if __name__ == '__main__' :
    header = {'user-agent': 'Indra Nugroho/indrafbrngrh@gmail.com'}

    url = 'https://www.themoviedb.org'
    next_url = '/tv/top-rated?page=1'
    
    i = 1
    show_array = []
    while next_url is not None:
        response = requests.get(url + next_url, headers=header, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        show_array += getData(soup)
        
        print('Page %d success' % i)
        
        try:
            next_url = (soup.find('div', attrs={'id': 'pagination_page_' + str(i)})).find('a')['href'].strip()
        except AttributeError:
            next_url = None

        i += 1

    with open('../data/TopRatedTVShowData.json', 'w') as outfile:
        json.dump(show_array, outfile, indent=4)