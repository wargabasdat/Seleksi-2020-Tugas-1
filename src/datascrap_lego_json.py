#!/usr/bin/env python
# coding: utf-8

# In[30]:


########## TUGAS SELEKSI 1 BASDAT ############
## Hollyana Puteri Haryono
## 18218013


# In[1]:


# library BeautifulSoup + request
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# In[2]:


# url utama 
my_url = 'https://www.lego.com/en-us/categories/age-12-plus-years?page='


# In[3]:


# array berisi keseluruhan product
product_containers = []


# In[4]:


# get html for each page
for i in range (1,51): 
    curr_url = my_url + str(i)
    uClient = uReq(curr_url)
    page_html = uClient.read()
    uClient.close()
    
    #html parser
    page_soup = soup(page_html, "html.parser")
    
    #grab each product
    containers = page_soup.findAll("li", {"data-test" : "product-item"})
    product_containers += containers


# In[5]:


# jumlah seluruh product yang didapat
len(product_containers)


# In[7]:


# list kosong untuk json file
products = {}


# In[26]:


# pemindahan data bersih dari array product_containers ke list
numb = 0
for container in product_containers:
    numb+=1
    #attribute name
    name = container.a["aria-label"]
    name.replace(",", "-")
    
    #attribute normal price
    raw_price_normal = container.find("span", {"data-test" : "product-price"}) 
    class_pn = str(type(raw_price_normal))
    price_normal = None

    if class_pn != "<class 'bs4.element.Tag'>" or class_pn != "<class 'NoneType'>" :
        price_str_normal = raw_price_normal.text
        l = list(price_str_normal)
    
        for i in range (1,6+1):
            del(l[0])
        price_str_normal = "".join(l)
        price_normal = float(price_str_normal) #convert string to float
    elif class_pn == "<class 'NoneType'>":
        price_normal = None        
    
    #attribute sale price
    raw_price_sale = container.find("span", {"data-test" : "product-price-sale"}) 
    class_ps = str(type(raw_price_sale))
    price_sale = None
    
    if class_ps == "<class 'bs4.element.Tag'>" or class_ps != "<class 'NoneType'>" :
        price_str_sale = raw_price_sale.text
        l = list(price_str_sale)
    
        for i in range (1,11+1):
            del(l[0])
        price_str_sale = "".join(l)
        price_sale = float(price_str_sale) #convert string to float
    elif class_ps == "<class 'NoneType'>":
        price_sale = None        
    
    #attribute rating
    raw_rating = container.find("div", {"class" : "RatingBar__RatingContainer-sc-1oakzec-1 crsdRv"})
    class_r = str(type(raw_rating))
    
    if class_r == "<class 'bs4.element.Tag'>" :
        rating_str = raw_rating["title"]
        rating = float(rating_str)
    else :
        rating = None

    #attribute status    
    raw_status = container.find("span", {"class" : "ProductBadge__StyledBadge-sc-1vris2w-0 cnlNTi"})
    class_s = str(type(raw_status))
    if class_s == "<class 'bs4.element.Tag'>" :
        status = raw_status.text
    else :
        status = None
    
    #input ke list
    products[name] = {
        'name' : name,
        'normal_price' : price_normal,
        'sale_price' : price_sale,
        'rating' : rating,
        'status' : status
    }
    
    # pengecekan tipe data masing-masing atribut dan data ke berapa
    print(type(name))
    print(type(price_normal))
    print(type(price_sale))
    print(type(rating))
    print(type(status))
    print(numb)


# In[27]:


# mengecek isi list products
print(products)


# In[28]:


# library json dan dump list ke json
import json
dump_product = json.dumps(products)
dump_product


# In[29]:


# melakukan write ke file json
with open (r"C:\Users\TEMP\Desktop\Belajar Pemograman\python\lego.json", "w") as f:
    f.write(dump_product)


# In[ ]:




