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
    
    # Extract nickname
    div = soup.find('div', class_='product_pricefrom')
    details['nickname'] = div.find('h2').text.strip().replace("'","")

    return details

    
def scrape_page(page_url):
    '''
    Scrape bath/shower products
    data from a single page
    '''

    # Creates a request
    r = requests.get(page_url, HEADER)

    # Initialize soup for html parsing
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    
    # Dictionary to hold data
    plants = []
    
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
        plants[i]['nickname'] = details[i]['nickname']

    return plants

def scrape():
    ''' Scrapes plants' data from various pages '''
    data['plants'] = []
    plants = data['plants']

    for i in range(4):
        if i == 0:
            plants.extend(scrape_page(URL))
        else:
            plants.extend(scrape_page(URL+"start.{}/".format(i+1)))
        time.sleep(1)         

def json_dump():
    ''' Dumps the dictionary as a json dump file '''

    with open('../data/plants.json', 'w') as out:
        out.write(json.dumps(data, indent=2))
    
    print("Data successfully saved to plants.json")
    
if __name__ == "__main__":
    scrape()
    json_dump()
