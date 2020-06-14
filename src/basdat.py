import bs4
import json
import string
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup

# class untuk membuat tuple dalam bentuk json
class Result:
    def __init__(self, scr_id, product_id, name, label, category, subcategory,real_price,sale_price):
        self.id = scr_id
        self.product_id = product_id
        self.name = name
        self.label = label
        self.category = category
        self.subcategory = subcategory
        self.real_price = real_price
        self.sale_price = sale_price

    def getJson(self):
        return {
            "id": self.id, 
            "product_id": self.product_id, 
            "name": self.name, 
            "label": self.label, 
            "category": self.category,
            "subcategory": self.subcategory,
            "real_price": self.real_price,
            "sale_price":self.sale_price
        }

# fungsi untuk mengumpulkan link2 untuk setiap kategori koleksi
def getNav(cat_container):
    # barang-barang new in
    new_in = cat_container.find("li", {"class" : "_category-link-wrapper menu-item menu-item--level-2 menu-item--is-leaf"})
    newin_atag = new_in.find("a", {"class" : "_category-link menu-item__category-link"})
    newin_link = newin_atag.get("href")
    navigators.append(newin_link)

    collection = cat_container.find("li", {"class" : "_category-link-wrapper menu-item menu-item--level-2 menu-item--current _displayUnfolded"})
    
    # untuk koleksi tanpa subkategori
    links = collection.find_all("li", {"class": "_category-link-wrapper menu-item menu-item--level-3 menu-item--is-leaf"})
    for i in range(len(links)):
        atag = links[i].find("a", {"class" : "_category-link menu-item__category-link"})
        if(atag):
            navigator = atag.get("href")
        else:
            navigator = "None"
        if(navigator!="None" and navigator and navigator not in navigators):
            navigators.append(navigator)

    # untuk koleksi dengan subkategori
    links = collection.find_all("li", {"class": "_category-link-wrapper menu-item menu-item--level-3"})
    for i in range(len(links)):
        subcat_ultag = links[i].find("ul", {"class" : "_subcategories subcategory-menu subcategory-menu--level-3"})
        subcats = subcat_ultag.find_all("li", {"class" : "_category-link-wrapper menu-item menu-item--level-4 menu-item--is-leaf"})
        for j in range(len(subcats)):
            subcat_name = subcats[j].get("data-name")
            if(subcat_name!="Lihat Semua"):
                subcat_atag = subcats[j].find("a", {"class" : "_category-link menu-item__category-link"})
                subcat_navigator = subcat_atag.get("href")
                subcat_navigator_2 = subcat_atag.get("data-href")
                if(subcat_navigator):
                    navigators.append(subcat_navigator)
                elif(subcat_navigator_2):
                    navigators.append(subcat_navigator_2)
            
    return navigators

# fungsi untuk mendapatkan kategori dan subkategori
def getCategory(cat_container):
    # barang-barang new in
    new_in = cat_container.find("li", {"class" : "_category-link-wrapper menu-item menu-item--level-2 menu-item--is-leaf"})
    cat_name = new_in.get("data-name")
    cat_tuple = (cat_name, "None")
    categories.append(cat_tuple)

    collection = cat_container.find("li", {"class" : "_category-link-wrapper menu-item menu-item--level-2 menu-item--current _displayUnfolded"})
    # untuk koleksi tanpa subkategori
    links = collection.find_all("li", {"class": "_category-link-wrapper menu-item menu-item--level-3 menu-item--is-leaf"})
    for i in range(len(links)):
        cat_name = links[i].get("data-name")
        if(cat_name!="Lihat Semua"):
            cat_tuple = (cat_name,"None")
            categories.append(cat_tuple)

    # untuk koleksi dengan subkategori
    links = collection.find_all("li", {"class": "_category-link-wrapper menu-item menu-item--level-3"})
    for i in range(len(links)):
        cat_name = links[i].get("data-name")
        subcat_ultag = links[i].find("ul", {"class" : "_subcategories subcategory-menu subcategory-menu--level-3"})
        subcats = subcat_ultag.find_all("li", {"class" : "_category-link-wrapper menu-item menu-item--level-4 menu-item--is-leaf"})
        for j in range(len(subcats)):
            subcat_name = subcats[j].get("data-name")
            if(subcat_name!="Lihat Semua"):
                cat_tuple = (cat_name,subcat_name)
                categories.append(cat_tuple)

    return categories

# mendapatkan HTML body dari page myurl
def getBody(myurl):
    headers = {'User-Agent': 'Chrome/5.0'}
    uClient = Request(myurl, headers=headers)
    page_html = urlopen(uClient).read()
    page_soup = soup(page_html,"html.parser")
    body = page_soup.body
    return body

# mendapatkan data koleksi wanita
def getData(navigators, categories):
    #menyimpan seluruh data barang
    data = [] 
    # menandakan sekarang sedang memparsing page categori yang mana
    cat_now = 0
    # jumlah produk / ID pada tuple json
    num_product = 1;
    for page in navigators:
        # print(cat_now, page)
        container = getBody(page)
        wraps = container.find_all("div",{"class":"_groups-wrap"})
        ultag = wraps[0].find("ul")
        litags = ultag.find_all("li")
        i=0
        for i in range(len(litags)):
            # get kode produk
            id = litags[i].get("id")
            product_info = litags[i].find("div", {"class": "product-info _product-info"})
            if(product_info):
                product_label = product_info.find("div", {"class" : "product-info-item product-info-item-label"})
                # get label produk
                if(product_label):
                    label = product_label.text
                else:
                    label = "None"
                product_name = product_info.find("a", {"class" : "name _item"})
                # get nama produk
                if(product_name):
                    name_temp = product_name.text
                    name_clean = name_temp.replace('\'', '')
                    name = name_temp.replace('\xa0', '')
                product_main_price = product_info.find("span", {"class" : "main-price"})
                # get harga barang ada 2 kasus
                # kasus 1 : bukan barang sale
                if(product_main_price):
                    main_price = product_main_price.get("data-price")
                    main_price_2 = main_price.replace(' IDR', '')
                    new_main_price = main_price_2.replace('.','')
                    # harga diskon kosong
                    new_price_sale = -1
                    res = Result(num_product, id, name, label, categories[cat_now][0], categories[cat_now][1] , int(new_main_price),int(new_price_sale))
                    data.append(res.getJson())
                    num_product+=1
                # kasus 2 : barang sale
                else:
                    product_main_price = product_info.find("span", {"class" : "line-through"})
                    product_price_sale = product_info.find("span", {"class" : "sale"})
                    # harga asli
                    if(product_main_price):
                        main_price = product_main_price.get("data-price")
                        main_price_2 = main_price.replace(' IDR', '')
                        new_main_price = main_price_2.replace('.','')
                    # harga diskon
                    if(product_price_sale):
                        price_sale = product_price_sale.get("data-price")
                        price_sale_2 = price_sale.replace(' IDR', '')
                        new_price_sale = price_sale_2.replace('.','')
                    res = Result(num_product, id, name, label, categories[cat_now][0], categories[cat_now][1] ,int(new_main_price),int(new_price_sale))
                    data.append(res.getJson())
                    num_product+=1
            i+=1
        cat_now+=1
    with open('../data/zara_women.json', 'w') as fp:
        fp.write(json.dumps(data, indent = 2))


# ------------------ Main Program ---------------------
# menyimpan link navigator untuk menuju page yang sesuai kategori
navigators = []
# menyimpan kategori dan subkategori barang dengan format tuple(kategori, subkategori)
categories = []

myurl = 'https://www.zara.com/id/id/woman-special-prices-l1314.html?v1=1446216'
container = getBody(myurl)
women_container = container.find("div",{"class" : "_container-nav navigation-menu"})
cat_container = women_container.find("li", {"class": "_category-link-wrapper menu-item menu-item--level-1 menu-item--current"})
print("getting the links...")
navigators = getNav(cat_container)
categories = getCategory(cat_container)
print("getting the datas")
getData(navigators, categories)
print("done!")