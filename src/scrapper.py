'''
Simple Web Scrapper Module

William Fu
13518055
'''
import time
import bs4
import requests
import json

BASE_URL = "https://www.crocus.co.uk"
URL = "https://www.crocus.co.uk/plants/_/"
HEADER = {'user-agent' : ' 	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0', 
          'from' : '13518055@std.stei.itb.ac.id' }

# Dictionary to hold data 
data = {}

def get_details(href):
    
    # Creates a request
    full_url = BASE_URL + href
    r = requests.get(full_url, HEADER)

    # Soup
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    details = {}

    # Review Count
    rating_count = soup.find('span', itemprop='ratingCount')
    details['rating-count'] = int(rating_count.text.strip()) if rating_count else 0

    # Avg rating
    avg_rating = soup.find('em', itemprop='ratingValue')
    details['avg-rating'] = int(avg_rating.text.strip()) if avg_rating else 0

    # Extract position
    prod_detail = soup.find('div', class_="productdt-top-left-wrap")
    li = prod_detail.find_all('li')
    details['position'] = li[0].text[10:].strip().split(" or ")
    details['soil'] = li[1].text[6:].strip().split(", ")
    details['rate-of-growth'] = li[2].text[16:].strip()
    
    details['flower-period'] = {} 
    f = details['flower-period']
    flower_period = li[3].text[18:].strip().split(" to ")
    f['start-month'] = flower_period[0]
    if len(flower_period) > 1:
        f['end-month'] = flower_period[1]
    else:
        f['end-month'] = None

    return details

    
def scrape_page():
    '''
    Scrape bath/shower products
    data from a single page
    '''

    # Creates a request
    r = requests.get(URL, HEADER)
    # print(r.text[:500])

    # Initialize soup for html parsing
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    
    # Dictionary to hold data
    data['plants'] = []
    plants = data['plants']
    
    # Scrape the plants' name
    details = []
    names = soup.find_all('h4', itemprop='name')
    for name in names :
        print(name.text.strip())
        for a in name.find_all('a', href=True) :
            c = get_details(a['href'])
            details.append(c)
            time.sleep(1)
    
    # Scrape the plants' pot property
    props = soup.find_all('span', itemprop='additionalProperty')

    # Scrape the plants'
    prices = soup.find_all('span', itemprop='price')
    
    # Scrapes the plants' availability
    avails = soup.find_all('span', class_='availability')
    
    # Appends to data
    n = len(names)
    for i in range(n):
        plant = {
            'name' : names[i].text.strip().replace("'",""),
            'prop' : props[i].text.strip(),
            'price' : float(prices[i].text.strip()[1:]),
            'availability' : avails[i].text.strip()
        }
        plants.append(plant)
    
    for i in range(n):
        plants[i]['rating'] = {
            'avg-rating' : details[i]['avg-rating'],
            'rating-count' : details[i]['rating-count']
        }
        plants[i]['position'] = details[i]['position']
        plants[i]['soil'] = details[i]['soil']
        plants[i]['rate-of-growth'] = details[i]['rate-of-growth']
        plants[i]['flower-period'] = details[i]['flower-period']


def json_dump():
    ''' Dumps the dictionary as a json dump file '''

    with open('../data/plants.json', 'w') as out:
        out.write(json.dumps(data, indent=2))

def go_to_link():

    # Creates a request
    r  = requests.get("https://www.crocus.co.uk/plants/_/alchemilla-mollis/classid.233/", HEADER)
    soup = bs4.BeautifulSoup(r.text, 'lxml')

    div = soup.find('div', class_='productdt-top-left-wrap')
    li = div.find_all('li')
    for l in li:
        print(l.text)
    print(li[0].text[10:].split(" or "))
    print(li[1].text[6:].split(", "))
    print(li[2].text[16:])
    print(li[3].text[18:].split(" to "))


    
if __name__ == "__main__":
    scrape_page()
    json_dump()
    # go_to_link()