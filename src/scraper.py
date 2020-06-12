# 135 18 034
# Program untuk men-scrape resep dari allrecipes.com

from requests import get
from bs4 import BeautifulSoup
from warnings import warn
import re, json

header = {'user-agent': 'Anindya Prameswari/pamsrewari@gmail.com'}

def scrape(url, req_no):
    global header
    response = get(url, headers = header)

    if response.status_code != 200:
        warn('Request {} fails with code {}. Continuing ...'.format(req_no, response.status_code))

    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('div', class_ = 'headline-wrapper')
    # beberapa halaman di /recipe/ memiliki struktur html yang berbeda, 
    # maka perlu dicek apakah halaman yang mau di-scrape memiliki 
    # struktur yang sama dengan struktur yang digunakan oleh scraper
    if name != None:
        data = {}
        data['id'] = re.search('\/recipe\/\d+\/', url).group()
        breadcrumb = soup.find_all('span', class_ = 'breadcrumbs__title')
        data['dessert-type'] = breadcrumb[3].text.strip()
        data['name'] = name.h1.text
        data['author'] = soup.find(class_ = 'author-name').text

        # get ratings
        stars = soup.find('span', class_ = 'review-star-text')
        if stars != None:
            rating = {}
            rating['stars'] = float(re.search('\d+(?:.\d+)?', stars.text).group())
            count = soup.find('span', class_ = 'ugc-ratings-item')
            rating['rated-by'] = int(re.search('\d+', count.text).group())
            data['rating'] = rating
        else:
            data['rating'] = '-'

        # get time
        time = {}
        meta_item = soup.find_all('div', class_ = 'recipe-meta-item')
        time['prep'] = meta_item[0].find('div', class_ = 'recipe-meta-item-body').text.strip()
        time['cook'] = meta_item[1].find('div', class_ = 'recipe-meta-item-body').text.strip()
        add = meta_item[3].find('div', class_ = 'recipe-meta-item-header').text.strip()
        if re.search('[Aa]dditional', add) != None:
            time['additional'] = meta_item[3].find('div', class_ = 'recipe-meta-item-body').text.strip()
        time['total'] = meta_item[2].find('div', class_ = 'recipe-meta-item-body').text.strip()
        data['time'] = time

        # get ingredients count
        ingredients_list = soup.find_all('li', class_ = 'ingredients-item')
        data['ingredients-count'] = len(ingredients_list)

        # get nutritions fact
        nutritions_section = soup.find('div', class_ = 'recipe-nutrition-section')
        nutritions_raw = nutritions_section.find('div', class_ = 'section-body').text.strip()
        nutritions = {}
        cal = re.search('\d+(?:\.\d+)?(?= calories)', nutritions_raw).group()
        if cal != None:
            nutritions['calories-in-cal'] = int(cal)
        fat = re.search('\d+(?:\.\d+)?(?= g tot)', nutritions_raw).group()
        if fat != None:
            nutritions['total-fat-in-gr'] = float(fat)
        chol = re.search('\d+(?:\.\d+)?(?= mg chol)', nutritions_raw).group()
        if chol != None:
            nutritions['cholesterol-in-mg'] = float(chol)
        sod = re.search('\d+(?:\.\d+)?(?= mg sod)', nutritions_raw).group()
        if sod != None:
            nutritions['sodium-in-mg'] = float(sod)
        carb = re.search('\d+(?:\.\d+)?(?= g carb)', nutritions_raw).group()
        if carb != None:
            nutritions['carb-in-gr'] = float(carb)
        pro = re.search('\d+(?:\.\d+)?(?= g pro)', nutritions_raw).group()
        if pro != None:
            nutritions['protein-in-gr'] = float(pro)
        data['nutritions-per-serving'] = nutritions

        print('Request {} succeeded.'.format(req_no))
        return data
    else:
        print('Request {} has a different HTML structure. Skipping ...'.format(req_no))

if __name__ == "__main__":
    url = 'https://www.allrecipes.com/recipes/79/desserts/?page='
    requests = 0

    for i in range(1, 41):
    # Dalam satu page /recipes/desserts/ ada kurang lebih 30 recipe cards
    # Akan ditelusuri 40 page untuk mendapatkan kira-kira 1200 recipe
        response = get(url + str(i), headers = header)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []

        recipe_cards = soup.find_all('article', class_ = 'fixed-recipe-card')
        for j in range(len(recipe_cards)):
            recipe_url = recipe_cards[j].div.a['href']
            requests += 1

            datum = scrape(recipe_url, requests)
            if data != None:
                data.append(datum)

    with open('../data/data.json', 'w') as f:
        json.dump(data, f, indent = 4)