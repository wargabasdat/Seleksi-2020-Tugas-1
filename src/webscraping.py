from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as bSoup
import csv, json
from csv import writer
import pandas as pd

def appendListAsRow(file_name, list_of_elmnt):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elmnt)

def getUrlData(some_url, file_name):

    #membuka koneksi, mengambil webpage
    uClient = uRequest(some_url)
    page = uClient.read()
    uClient.close()

    #HTML parser
    page_soup = bSoup(page, "html.parser")

    #mengambil data produk
    products = page_soup.findAll("li", {"class": "product"})

    #menuliskan ke dalam suatu format tertentu
    for product in products:
        code = product.p.text

        title = product.findAll("h4", {"class": "card-title"})
        name = title[0].text.strip()

        price = product.findAll("span", {"class": "price price--withoutTax"})
        price_without_tax = price[0].text

        product_types = page_soup.findAll("h1", {"class": "cat-heading"})
        product_type = product_types[0].text

        stars = product.findAll("span", {"class": "icon icon--ratingFull"})
        rating = len(stars)

        elmnt = [code, name, price_without_tax, product_type, rating]
        appendListAsRow(file_name, elmnt)

#membuat csv
file_name = "leica.csv"
f = open(file_name, "w")
headers = "code, name, price_without_tax, type, rating\n"
f.write(headers)
f.close()

#mendapatkan data dari url
getUrlData("https://leicacamerausa.com/photography/leica-m/m-cameras/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-m/m-lenses/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-m/m-lenses/?sort=pricedesc&page=2", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-m/m-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-m/m-cases-protectors/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-m/m-cases-protectors/?sort=pricedesc&page=2", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-q/q-cameras/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-q/q-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-q/q-protectors/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-sl/sl-camera/", file_name)
getUrlData("https://leicacamerausa.com/photography/l-mount/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-sl/sl-camera-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-s/s-camera/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-s/s-lenses/lens-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-s/s-lenses/s-lens-adapters/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-s/s-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-s/s-accessories/?sort=pricedesc&page=2", file_name)
getUrlData("https://leicacamerausa.com/photography/leica-s/s-protectors/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-cl/cl-cameras/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-cl/cl-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-cl/cl-protectors/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-cl/cl-protectors/?sort=pricedesc&page=2", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-tl/tl-cameras/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-tl/tl-accessories/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-tl/tl-protectors/", file_name)
getUrlData("https://leicacamerausa.com/photography/aps-c-system/leica-tl/tl-protectors/?sort=pricedesc&page=2", file_name)
getUrlData("https://leicacamerausa.com/photography/compact-cameras/", file_name)
getUrlData("https://leicacamerausa.com/photography/lens-filters/", file_name)
getUrlData("https://leicacamerausa.com/photography/lens-filters/?sort=alphaasc&page=2", file_name)
getUrlData("https://leicacamerausa.com/photography/lens-filters/?sort=alphaasc&page=3", file_name)
getUrlData("https://leicacamerausa.com/photography/tripods/", file_name)

csvFilePath = "leica.csv"
jsonFilePath = "leica.json"

#membaca scv dan menambahkan ke data
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["code"]
        data[id] = rows

#membuat json file dan menuliskan data
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))