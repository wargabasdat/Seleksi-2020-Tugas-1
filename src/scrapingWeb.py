import requests
from bs4 import BeautifulSoup
import pymongo
from time import sleep
import json

# Accessing the HTML content from webpage
HEADER = {'User-Agent' : 'Mozilla/5.0 (Windows);Basis Data/13518067@std.stei.itb.ac.id'}

# get url desc from database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["berBen"]

def getdata(category):
    # To get list url to scrape
    page_one = ["shoes/flats","shoes/sneakers","shoes/sandals","shoes/loafers","accessories/belts","accessories/eyewear","accessories/watches","clothing/bottoms/culottes","clothing/bottoms/jeans","clothing/bottoms/leggings","clothing/bottoms/short-pants","clothing/dresses/bodycon","clothing/dresses/casual","clothing/dresses/maxi-dresses"]
    page_two = ["clothing/bottoms/long-pants","clothing/bottoms/skirts","clothing/dresses/jumpsuit","clothing/dresses/midi-dresses","clothing/dresses/mini-dresses","clothing/outerwear/blazers","clothing/outerwear/kimono","clothing/outerwear/vest"]
    if "earrings" in category or "scarves" in category or category in page_two:
        URLS = ["https://berrybenka.com/"+category+"/women","https://berrybenka.com/"+category+"/women/48"]
    elif category in page_one or "bags" in category or "outerwear" in category:
        URLS = ["https://berrybenka.com/"+category+"/women"]
    else:
        URLS = ["https://berrybenka.com/"+category+"/women","https://berrybenka.com/"+category+"/women/48","https://berrybenka.com/"+category+"/women/96"]
    for URL in URLS:
        response = requests.get(URL, headers=HEADER)

        # Parsing the HTML content
        page_html = response.content
        page_soup = BeautifulSoup(page_html, 'lxml')

        # results from scrape
        quotes = []
        elmt = page_soup.find('ul',attrs={'id':'ul-catalog'})
        for li in elmt.find_all('li',attrs={'id':'li-catalog'}):
            quote = {}
            quote['url'] = li.a['href']
            quote['img'] = li.find('div',attrs={'class':'catalog-image'}).img['src']
            quote['price'] = int(li.find('div',attrs={'class':'detail-right'}).find('p').get_text().replace("IDR ","").replace(".",""))
            quote['discount'] = int(li.find('div',attrs={'class':'detail-right'}).find('p',attrs={'class':'discount'}).get_text().replace("IDR ","").replace(".",""))
            quote['name'] = li.find('div',attrs={'class':'detail-left'}).h1.text
            quotes.append(quote)
    sleep(2)
    return quotes

clothingTop = ["clothing/tops/blouse","clothing/tops/women-shirts"]
clothingBottom = ["clothing/bottoms/culottes","clothing/bottoms/jeans","clothing/bottoms/leggings","clothing/bottoms/long-pants","clothing/bottoms/short-pants","clothing/bottoms/skirts"]
clothingDress = ["clothing/dresses/bodycon","clothing/dresses/casual","clothing/dresses/maxi-dresses","clothing/dresses/midi-dresses","clothing/dresses/mini-dresses"]
clothingOut = ["clothing/outerwear/blazers","clothing/outerwear/cardigans","clothing/outerwear/coats","clothing/outerwear/jackets","clothing/outerwear/kimono","clothing/outerwear/sweaters","clothing/outerwear/vest"]
shoes = ["shoes/mules","shoes/flats","shoes/heels","shoes/sneakers","shoes/sandals","shoes/loafers"]
bags = ["bags/big-bags","bags/small-bags","bags/clutch-bag","bags/wallets","bags/backpack"]
accessories = ["accessories/earrings","accessories/scarves","accessories/belts","accessories/eyewear","accessories/watches"]

def insert2db(category,arr):
    # insert to database
    for elmt in arr:
        quotes = getdata(elmt)
        x = elmt.split("/")
        file = x[-1].replace("-","_")+".json"
        with open(file,'w') as f:
            f.write('[')
            idx = 0
            for quote in quotes:
                if "clothing" in elmt:
                    dataScrape = { # record
                        "category":category,
                        "tag":x[-2],
                        "url":quote['url'],
                        "image":quote['img'],
                        "price":quote['price'],
                        "discount":quote['discount'],
                        "name":quote['name'] 
                    }
                else:
                    dataScrape = { # record
                        "category":category,
                        "url":quote['url'],
                        "image":quote['img'],
                        "price":quote['price'],
                        "discount":quote['discount'],
                        "name":quote['name']
                    }

                # write to json file
                json.dump(dataScrape,f)
                if idx < len(quotes)-1:
                    f.write(',\n')
                idx += 1
                # insert to mongodb
                mydb[x[-1].replace("-","_")].insert_one(dataScrape)
            f.write(']')

# insert to database : done
insert2db("shoes",shoes)
insert2db("bags",bags)
insert2db("accessories",accessories)
insert2db("clothing",clothingTop)
insert2db("clothing",clothingBottom)
insert2db("clothing",clothingOut)
insert2db("clothing",clothingDress)

def getdesc(collname,f,g,h,l,j,k):
    top = ["blouse","women_shirts"]
    bottom = ["culottes","jeans","leggings","long_pants","short_pants","skirts"]
    dress = ["bodycon","casual","jumpsuit","maxi_dresses","midi_dresses","mini_dresses"]
    out = ["blazers","cardigans","coats","jackets","kimono","sweaters","vest"]
    shoes = ["mules","flats","heels","sneakers","sandals","loafers"]
    bags = ["big_bags","small_bags","clutch_bag","wallets","backpack"]
    accessories = ["earrings","scarves","belts","eyewear","watches"]
    data = mydb[collname].find({},{"_id":1,"url":1})
    # quotes = []
    for idx,x in enumerate(data):
        URL = x["url"]
        response = requests.get(URL, headers=HEADER)
        # Parsing the HTML content
        page_html = response.content
        page_soup = BeautifulSoup(page_html, 'lxml')

        # results from scrape to quote
        elmt = page_soup.find('div',attrs={'class':'prod-desc-wrapper'})
        warna = []
        for w in elmt.find('ul',attrs={'id':'filter-color'}).find_all('li'):
            warna.append(w.label['data-original-title'])
        size = []
        for s in elmt.find('ul',attrs={'id':'select-size'}).find_all('li'):
            size.append(s.label.text.replace("\n","").replace(" ",""))
        bahan = ""
        perawatan = ""
        for p in elmt.find('div',attrs={'care'}).find_all('p'):
            if "Bahan" in p.get_text():
                bahan = p.get_text().replace("Bahan","").replace("\n","").replace(":","").replace(" ","").replace("\u00a0","")
            if "Perawatan" in p.get_text():
                perawatan = p.get_text().replace("\n"," ").replace("Perawatan","").replace(":","")
        rincianUkuran = []
        SizeUkuran = ""
        list_p = elmt.find('div',attrs={'class':'sizing-care'}).find('ul').find_all('p')
        for i,p in enumerate(list_p):
            if collname in top or collname in bottom or collname in out or collname in dress:
                if "Model" not in p.get_text() and "cm" in p.get_text():
                    rincian = ""
                    if "Ukuran" not in p.get_text() and "Size" not in p.get_text():
                        rincian = "Ukuran ONESIZE\n"
                    rincian += p.get_text().replace("\xa0","").replace("Ukuran","Ukuran:").replace("Panjang Baju","Panjang").replace("Size","Size:").replace(" ","").replace(":"," ").replace("cm","").replace(" Baju","\nBaju")
                    rincianUkuran.append(rincian[-1])
                    arr = rincian.split("\n")
                    ukuran = arr[0].replace("Ukuran","").replace("Size","").replace(" ","")
                    tipe = ""
                    lebarBahu = "0"
                    lingkarDada = "0"
                    panjangTangan = "0"
                    lingkarLengan = "0"
                    lingkarPinggang = "0"
                    lingkarPaha = "0"
                    lingkarPinggul = "0"
                    pesak = "0"
                    panjang = "0"
                    for elm in (arr):
                        y = elm.split(" ")
                        if "Baju" in elm:
                            tipe = y[-1]
                        elif "Bahu" in elm:
                            lebarBahu = y[-1].split("-")[-1]
                        elif "Dada" in elm:
                            lingkarDada = y[-1].split("-")[-1]
                        elif "Tangan" in elm:
                            panjangTangan = y[-1].split("-")[-1]
                        elif "Lengan" in elm:
                            lingkarLengan = y[-1].split("-")[-1]
                        elif "Pinggang" in elm or "Waist" in elm:
                            lingkarPinggang = y[-1].split("-")[-1]
                        elif "Pinggul" in elm or "Hip" in elm:
                            lingkarPinggul = y[-1].split("-")[-1]
                        elif "Paha" in elm:
                            lingkarPaha = y[-1].split("-")[-1]
                        elif "Pesak" in elm:
                            pesak = y[-1].split("-")[-1]
                        else:
                            panjang = y[-1].split("-")[-1]
                        if "BajuDalam" in elm:
                            SizeUkuran = ukuran
                        if "BajuLuar" in elm:
                            ukuran = SizeUkuran
                    if ukuran == "":
                        ukuran = "ONESIZE"
                    if collname in top:
                        # write to json file
                        json.dump({
                            "id_produk":str(x["_id"]),
                            "Ukuran":ukuran,
                            "Tipe":tipe,
                            "Lebar bahu":int(lebarBahu),
                            "Lingkar Dada":int(lingkarDada),
                            "Panjang Tangan":int(panjangTangan),
                            "Lingkar Lengan":int(lingkarLengan),
                            "Lingkar Pinggang":int(lingkarPinggang),
                            "Panjang":int(panjang)
                        },g)
                        g.write(",\n")
                        # insert to database
                        mydb["rincian_ukuran_top"].insert_one({
                            "id_produk":x["_id"],
                            "Ukuran":ukuran,
                            "Tipe":tipe,
                            "Lebar bahu":int(lebarBahu),
                            "Lingkar Dada":int(lingkarDada),
                            "Panjang Tangan":int(panjangTangan),
                            "Lingkar Lengan":int(lingkarLengan),
                            "Lingkar Pinggang":int(lingkarPinggang),
                            "Panjang":int(panjang)
                        })
                    elif collname in bottom:
                        # write to json file
                        json.dump({
                            "id_produk":str(x["_id"]),
                            "Ukuran":ukuran,
                            "Lingkar Pinggang":int(lingkarPinggang),
                            "Lingkar Pinggul":int(lingkarPinggul),
                            "Lingkar Paha":int(lingkarPaha),
                            "Pesak":int(pesak),
                            "Panjang":int(panjang)
                        },h)
                        h.write(",\n")
                        # insert to database
                        mydb["rincian_ukuran_bottom"].insert_one({
                            "id_produk":x["_id"],
                            "Ukuran":ukuran,
                            "Lingkar Pinggang":int(lingkarPinggang),
                            "Lingkar Pinggul":int(lingkarPinggul),
                            "Lingkar Paha":int(lingkarPaha),
                            "Pesak":int(pesak),
                            "Panjang":int(panjang)
                        })
                    elif collname in out or collname in dress:
                        # write to json file
                        json.dump({
                            "id_produk":str(x["_id"]),
                            "Ukuran":ukuran,
                            "Lebar bahu":int(lebarBahu),
                            "Lingkar Dada":int(lingkarDada),
                            "Panjang Tangan":int(panjangTangan),
                            "Lingkar Lengan":int(lingkarLengan),
                            "Lingkar Pinggang":int(lingkarPinggang),
                            "Panjang":int(panjang)
                        },l)
                        l.write(",\n")
                        # insert to database
                        mydb["rincian_ukuran_outer_dress"].insert_one({
                            "id_produk":x["_id"],
                            "Ukuran":ukuran,
                            "Lebar bahu":int(lebarBahu),
                            "Lingkar Dada":int(lingkarDada),
                            "Panjang Tangan":int(panjangTangan),
                            "Lingkar Lengan":int(lingkarLengan),
                            "Lingkar Pinggang":int(lingkarPinggang),
                            "Panjang":int(panjang)
                        })
            elif collname in bags:
                rincian = p.get_text().replace("cm","").replace(" ","").replace(":"," ").split("\n")
                tinggi = "0"
                lebar = "0"
                alas = "0"
                tali = "0"
                for elm in rincian:
                    if  "Tinggi" in elm:
                        tinggi = elm.split(" ")[-1].split("-")[-1].replace(",",".")
                    elif "Lebar" in elm:
                        lebar = elm.split(" ")[-1].split("-")[-1].replace(",",".")
                    elif "Alas" in elm:
                        alas = elm.split(" ")[-1].split("-")[-1].replace(",",".")
                    elif "Tali" in elm:
                        tali = elm.split(" ")[-1].split("-")[-1].replace(",",".")
                if i == 1:
                    # write to json file
                    json.dump({
                        "id_produk":str(x["_id"]),
                        "Tinggi":float(tinggi),
                        "Lebar":float(lebar),
                        "Alas":float(alas),
                        "Panjang Tali":float(tali)
                    },j)
                    j.write(",\n")
                    # insert to database
                    mydb["rincian_ukuran_bags"].insert_one({
                        "id_produk":x["_id"],
                        "Tinggi":float(tinggi),
                        "Lebar":float(lebar),
                        "Alas":float(alas),
                        "Panjang Tali":float(tali)
                    })
                elif i==3:
                    # write to json file
                    json.dump({
                        "id_produk":str(x["_id"]),
                        "Tinggi":float(tinggi),
                        "Lebar":float(lebar),
                        "Alas":float(alas),
                        "Panjang Tali":float(tali)
                    },k)
                    k.write(",\n")
                    # insert to database
                    mydb["rincian_ukuran_additional_bags"].insert_one({
                        "id_produk":x["_id"],
                        "Tinggi":float(tinggi),
                        "Lebar":float(lebar),
                        "Alas":float(alas),
                        "Panjang Tali":float(tali)
                    })
        # write to json file
        json.dump({
            "id_produk":str(x["_id"]),
            "description":elmt.find('div',attrs={'class':'prod-wording'}).p.text.replace("\u00a0"," ").replace("\n","\n ").replace("\n ",""),
            "warna":warna,
            "size":size,
            "bahan":bahan,
            "perawatan":perawatan
        },f)
        f.write(',\n')
        # insert to database
        mydb["desc_produk"].insert_one({
            "id_produk":x["_id"],
            "description":elmt.find('div',attrs={'class':'prod-wording'}).p.text.replace("\u00a0"," ").replace("\n","\n ").replace("\n ",""),
            "warna":warna,
            "size":size,
            "bahan":bahan,
            "perawatan":perawatan
        })
        sleep(2)


# insert description produk to database : done
with open('dataDescScrape.json','w') as f:
    with open('dataRincianClothingTop.json','w') as g:
        with open('dataRincianClothingBottom.json','w') as h:
            with open('dataRincianClothingOutDress.json','w') as i:
                with open('dataRincianBags.json','w') as j:
                    with open('dataRincianAddBag.json','w') as k:
                        f.write('[')
                        g.write('[')
                        h.write('[')
                        i.write('[')
                        j.write('[')
                        k.write('[')
                        for x in mydb.list_collection_names():
                            getdesc(x,f,g,h,i,j,k)
                        f.write(']')
                        g.write(']')
                        h.write(']')
                        i.write(']')
                        j.write(']')
                        k.write(']')