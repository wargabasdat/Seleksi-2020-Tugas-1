#Muhamad Hudan Widzamil
#18218003
#Sistem dan Teknologi Informasi ITB

from bs4 import BeautifulSoup
import urllib.request
import json

print("Geekbench Android Benchmark Chart Scraper")
print("gathered from https://browser.geekbench.com/android-benchmarks/")
url = 'https://browser.geekbench.com/android-benchmarks/'
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page,'html.parser')

single = soup.find('div',{'id':'single-core'}) #segmen single core
multi = soup.find('div',{'id':'multi-core'}) #segmen multi core

#pengambilan daftar nama ponsel, soc, dan hasil benchmark bagian single core
singlephone = single.find_all('a',{'href':lambda L: L and L.startswith('/android_devices/')})
singleprocie = single.find_all('div',{'class':'description'})
singlecore = single.find_all('td',{'class':'score'})

#pengambilan daftar nama ponsel, soc, dan hasil benchmark bagian multi core
multiphone = multi.find_all('a',{'href':lambda L: L and L.startswith('/android_devices/')})
multicore = multi.find_all('td',{'class':'score'})
multiprocie = multi.find_all('div',{'class':'description'})


data = []
#masukan data tiap ponsel ke list
for i in range (len(singlephone)):
    temp = []
    #menambahkan nama ponsel
    temp.append(singlephone[i].contents[0].strip("\n"))
    #menambahkan nama soc
    temp.append(singleprocie[i].contents[0].strip("\n").split(" @ ")[0])
    #menambahkan clock speed
    temp.append(float(singleprocie[i].contents[0].strip("\n").split(" @ ")[1].split(" ")[0]))
    #menambahkan hasil benchmark single core
    temp.append(int(singlecore[i].contents[0]))
    #menambahkan hasil benchmark multi core
    #menyesuaikan dengan nama ponsel karena index pada single core dan multicore tidak merujuk pada device yang sama
    for j in range(len(multiphone)):
        if (multiphone[j].contents[0].strip("\n"))==temp[0] and (multiprocie[j].contents[0].strip("\n").split(" @ ")[0])==temp[1]:
            temp.append(int(multicore[j].contents[0]))
    data.append(temp)
#diubah menjadi json
final_list = [{"name":x[0],"processor":x[1],"clockspeed":x[2],"score":{"singlecore":x[3],"multicore":x[4]}} for x in data]

#menyimpan hasil ke file eksternal
with open('../data/data.json', 'w') as outfile:
    json.dump(final_list, outfile)

print("Data scraped successfully")

