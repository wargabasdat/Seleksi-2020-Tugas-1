# 135 18 034
# Program untuk men-scrape resep dari allrecipes.com

from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep, time
import re, json

header = {'user-agent': 'Anindya Prameswari/pamsrewari@gmail.com'}

def convertToMinute(text):
    hr = re.search('(?:\d+)(?= hr)', text)
    mn = re.search('(?:\d+)(?= min)', text)

    total = 0
    if hr != None:
        total += int(hr.group()) * 60
    if mn != None:
        total += int(mn.group())

    return total

def scrape(url, req_no):
    global header
    response = get(url, headers = header)

    if response.status_code != 200:
        warn('Request {} fails with code {}. Continuing ...'.format(req_no, response.status_code))
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('div', class_ = 'headline-wrapper')
    # beberapa halaman di /recipe/ memiliki struktur html yang berbeda, 
    # maka perlu dicek apakah halaman yang mau di-scrape memiliki 
    # struktur yang sama dengan struktur yang digunakan oleh scraper
    if name != None:
        try:
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

            for t in range(len(meta_item)):
                prep = meta_item[t].find('div', class_ = 'recipe-meta-item-header').text
                if (re.search('[Pp]rep', prep)):
                    text = meta_item[t].find('div', class_ = 'recipe-meta-item-body').text.strip()
                    time['prep'] = convertToMinute(text)
                    break

            for t in range(len(meta_item)):
                cook = meta_item[t].find('div', class_ = 'recipe-meta-item-header').text
                if (re.search('[Cc]ook', cook)):
                    text = meta_item[t].find('div', class_ = 'recipe-meta-item-body').text.strip()
                    time['cook'] = convertToMinute(text)
                    break
            
            for t in range(len(meta_item)):
                add = meta_item[t].find('div', class_ = 'recipe-meta-item-header').text
                if (re.search('[Aa]dditional', add)):
                    text = meta_item[t].find('div', class_ = 'recipe-meta-item-body').text.strip()
                    time['additional'] = convertToMinute(text)
                    break

            for t in range(len(meta_item)):
                total = meta_item[t].find('div', class_ = 'recipe-meta-item-header').text
                if (re.search('[Tt]otal', total)):
                    text = meta_item[t].find('div', class_ = 'recipe-meta-item-body').text.strip()
                    time['total'] = convertToMinute(text)
                    break
                
            if time:
                data['time'] = time
            else:
                data['time'] = '-'

            # get ingredients count
            ingredients_list = soup.find_all('li', class_ = 'ingredients-item')
            data['ingredients-count'] = len(ingredients_list)

            # get nutritions fact
            nutritions_section = soup.find('div', class_ = 'recipe-nutrition-section')
            nutritions_raw = nutritions_section.find('div', class_ = 'section-body').text.strip()
            nutritions = {}
            cal = re.search('\d+(?:\.\d+)?(?= calories)', nutritions_raw)
            if cal != None:
                nutritions['calories-in-cal'] = float(cal.group())
            fat = re.search('\d+(?:\.\d+)?(?= g tot)', nutritions_raw)
            if fat != None:
                nutritions['total-fat-in-gr'] = float(fat.group())
            chol = re.search('\d+(?:\.\d+)?(?= mg chol)', nutritions_raw)
            if chol != None:
                nutritions['cholesterol-in-mg'] = float(chol.group())
            sod = re.search('\d+(?:\.\d+)?(?= mg sod)', nutritions_raw)
            if sod != None:
                nutritions['sodium-in-mg'] = float(sod.group())
            carb = re.search('\d+(?:\.\d+)?(?= g carb)', nutritions_raw)
            if carb != None:
                nutritions['carb-in-gr'] = float(carb.group())
            pro = re.search('\d+(?:\.\d+)?(?= g pro)', nutritions_raw)
            if pro != None:
                nutritions['protein-in-gr'] = float(pro.group())
            data['nutritions-per-serving'] = nutritions

            print('Request {} succeeded.'.format(req_no))
            return data
        except:
            print('Request {} met an exception. Passing ...'.format(req_no))
            return None
    else:
        print('Request {} has a different HTML structure. Skipping ...'.format(req_no))
        return None

if __name__ == "__main__":
    url = 'https://www.allrecipes.com/recipes/79/desserts/?page='
    requests = 0
    print('Starting ...')
    data = []

    for i in range(1, 51):
    # Dalam satu page /recipes/desserts/ ada kurang lebih 20 recipe cards
    # Akan ditelusuri 50 page untuk mendapatkan kira-kira 1000 resep
        response = get(url + str(i), headers = header)
        soup = BeautifulSoup(response.text, 'html.parser')

        recipe_cards = soup.find_all('article', class_ = 'fixed-recipe-card')
        for j in range(len(recipe_cards)):
            start = time()
            recipe_url = recipe_cards[j].div.a['href']
            requests += 1
            sleep(1)

            datum = scrape(recipe_url, requests)
            if datum != None:
                data.append(datum)
            print('Elapsed time: {}'.format(time() - start))

    with open('../data/data.json', 'w') as f:
        json.dump(data, f, indent = 4)

# Single Scrape Test
# url = 'https://www.allrecipes.com/recipe/278238/maamoul-lebanese-date-cookies/'
# data = scrape(url, 2)
# print(data)