import urllib.request
from bs4 import BeautifulSoup as soup
import time
import json
import os

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

#mengembalikan merek
def parseLogo(brand) :
    count = 0
    index = []
    logo = ""
    #mencari berapa "-" dan di index mana saja
    for i in range (len(brand)) :
        if brand[i] == "-" :
            index.append(i)
    
    #mengambil nama merek
    countIndex = len(index)
    awal = index[0]+1
    if countIndex > 3  :
        awal = index[0]+1
        akhir = index[countIndex-2]-1
    else :
        akhir = index[countIndex-1]-1
    for i in range (awal, akhir+1) :
        logo += brand[i]
    
    #merek : cotton-on-foundation/cotton-on women/cotton-on-men/cotton-on-kids
    if "foundation" in brand :
        logo += "-foundation"
    elif "women" in brand :
        logo += "-women"
    elif "men" in brand :
        logo += "-men"
    elif "kids" in brand :
        logo += "-kids"
    
    #menghapus warna logo
    if "pink" in logo :
        idx = logo.find("pink")
        logo = logo[:(idx-1)]
    elif "green" in logo :
        idx = logo.find("green")
        logo = logo[:(idx-1)]
      
    return logo

#mengembalikan harga promo dengan tipe float
def parsePromo(promo,realPrice):
    countProduct = ""
    price = ""
    discount = ""

    #ex : 2 FOR $30, maka harga promo : $15
    if "for" in promo.lower() :
        i = 0
        while promo[i] != " " :
            countProduct += promo[i]
            i+=1
        priceIdx = promo.find("$")
        price = promo[priceIdx+1:]
        promoPrice = float(price) / float(countProduct)

    #ex: BUY ONE GET ONE 50% OFF, maka harga promo 50%*harga asli
    elif "get" in promo.lower() :
        percentIdx = promo.find("%")
        i = percentIdx
        found = False
        while not found and i>=0:
            if promo[i] == " " :
                found = True
            else :
                i-=1
        for i in range (i+1,percentIdx) :
            discount += promo[i]
        
        promoPrice = realPrice * (100-float(discount)) / 100
        
    #ex: 20% OFF, maka harga promo 80%*harga asli
    elif "off" in promo.lower() :
        i = 0
        while promo[i] != "%" :
            discount+= promo[i]
            i+=1
        promoPrice = realPrice * (100-float(discount)) / 100

    #ex: NOW $5, maka harga promo = $5
    elif "now" in promo.lower():
        dollarIdx = promo.find("$")
        promoPrice = float(promo[(dollarIdx+1):])
    

    else :
        print("beda")
        promoPrice = realPrice
    
    promoPrice = ("{:.2f}".format(promoPrice))
        
    return float(promoPrice)

#mengambil total page yang harus ditelusuri
def parseTotalPage(items) :
    i = 0
    finish = False
    total = ""
    while not finish and i<len(items):
        if items[i] == " " :
            finish = True
        else :
            if items[i] != "," :
                total += items[i]
        i+=1

    page = int(int(total) / 48) + 1
    return page   

#mengambil price dari string to float 
def priceToFloat(price):
    res = price[1:]
    return float(res)


def parse(page_soup, records) :
    products = page_soup.findAll("li",{"class":"grid-tile columns"})

    for product in products :
        #nama
        name = product.find("div",{"class":"product-name"}).a.text.strip()
        if " Mens " not in name:
            #harga
            price1 = product.find("div",{"class":"product-pricing"}).find("span",{"title":"Standard Price"}).text
            price = priceToFloat(price1)

            #warna
            color = int(product.find("div",{"class":"product-colours-available"}).span.text)

            #brand
            brand1 = product.find("div",{"class":"product-brand"})
            if brand1.span != None :
                brand2 = brand1.span.span.get("class")[1]
                brand = parseLogo(brand2)
            else : 
                brand = product.find("div",{"class":"product-brand"}).text.strip()

            #promo
            promo1 = product.find("div",{"class":"product-promo"})
            #tidak ada keterangan promo 
            if promo1 == None :
                #ada harga baru
                if product.find("div",{"class":"product-pricing"}).find("span",{"title":"Sale Price"}) != None :
                    salesPrice = product.find("div",{"class":"product-pricing"}).find("span",{"title":"Sale Price"}).text
                    AngkaPromo = (100-(priceToFloat(salesPrice)/price))
                    promo = str("{:.2f}".format(AngkaPromo))+"% OFF"
                #tidak ada promo
                else :
                    promo = "Tidak ada promo"
            else :
                promo = promo1.find("div",{"class":"promotional-message"}).text.strip()

            #harga promo
            #tidak ada keterangan promo 
            if promo1 == None : 
                #ada harga baru
                if product.find("div",{"class":"product-pricing"}).find("span",{"title":"Sales Price"}) != None :
                    promoPrice = priceToFloat(product.find("div",{"class":"product-pricing"}).find("span",{"title":"Sales Price"}).text)
                #tidak ada promo
                else :
                    promoPrice = price
            else :
                promoPrice = parsePromo(promo,price)    
            record = {
                "Nama" : name,
                "Harga($)" : price,
                "KetersediaanWarna" : color,
                "Merek" : brand,
                "Promo" : promo,
                "HargaPromo($)" : promoPrice
            }
            # print(record)
            #menghilangkan product yang double
            if record not in records :
                records.append(record)

    return records

def openConnection(url) :
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read()
    urllib.request.urlopen(request).close()

    page_soup = soup(html,"html.parser")

    return page_soup

#MAIN
try :
    url = "https://cottonon.com/AU/women/"

    records = []

    page_soup = openConnection(url)

    items1 = page_soup.find("span",{"class":"paging-information-items"}).text
    pages = parseTotalPage(items1.strip())

    for i in range (pages+1) :
        print(i+1)
        page = "page-"+str(i+2)
        records = parse(page_soup,records)
        if (i+1 < (pages)) :
            url = page_soup.find("a",{"class":page}).get("href")
            page_soup = openConnection(url)
    
    current_directory = os.getcwd()
    parent_directory = os.path.split(current_directory)[0]
    with open((parent_directory+'/data/data.json'), 'w') as json_file:
    json.dump(records, json_file)

    print(len(records))
    
except :
    print("error occured")