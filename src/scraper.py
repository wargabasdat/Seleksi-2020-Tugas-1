import requests
import json
from bs4 import BeautifulSoup

def getID(link):
    #Mendapatkan ID video
    last = -1
    for i in range(len(link)):
        if(link[i]=="/"):
            last = i+1
    return link[last:]

def inputListToData(tipe,ctr,category,name,value):
    if(category=="seasons"):
        data[tipe][ctr][category] = []
        for i in seasons:
            data[tipe][ctr][category].append({
                'name' : i[2],
                'type' : i[0],
                'dateCreated' : i[1],
                'numberOfEpisodes' : i[3],
            })
    else:
        data[tipe][ctr][category] = []
        for i in value :
            data[tipe][ctr][category].append({
                name : i
            })

set_error = {"https://www.iflix.com/id/en/play/short/259132","https://www.iflix.com/id/en/play/short/260079","https://www.iflix.com/id/en/play/short/259109"} # Set link yang tidak normal dalam iflix.com
set_link = set() # Set yang berisi page-page yang ada di iflix.com
set_movser = set() # Set yang berisi link movies/series/clip yang ada di iflix.com

data = {} #dictionaries untuk menyimpan data hasil ekstraksi
data['TVSeries'] = []
data['Movie'] = []
data['Clip'] = []

ctr_movies = 0
ctr_tvseries = 0

fileName = input('Input file name (ex: "data_results.json") : ')

print("Getting Link....")
# headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64); Basis Data/Admin Basis Data/basisdata@std.stei.itb.ac.id'}
result = requests.get("https://www.iflix.com/id/en/browse")
src = result.content
soup = BeautifulSoup(src, 'lxml')

#Mengambil link movies/series yang ada di Homepage
a = soup.find_all("a",class_="Assetstyled__Asset-sc-10ot425-0 AuoqH Assetenhanced__AssetPoster-sc-4qqccm-0 jcOpMq inline-functions")
for link in a:
    set_movser.add(str(link.get('href')))

## Mendapatkan link page-page yang ada di iflix.com 
b = soup.find_all("a",class_="Tabstyled__TabButton-aei9xz-0 kxBaBd")
for link in b:
    set_link.add(str(link.get('href')))

## Mencari seluruh link movies/series yang ada di setiap page iflix.com
for i in set_link:
    link = "https://www.iflix.com" + i
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    a = soup.find_all("a",class_="Assetstyled__Asset-sc-10ot425-0 AuoqH Assetenhanced__AssetPoster-sc-4qqccm-0 jcOpMq inline-functions")
    
    for link in a:
        set_movser.add(str(link.get('href')))


print("Getting Link Completed")

counter = 0 #jumlah data yang bisa diekstraksi
counter2 = 0 #jumlah data yang berhasil diekstraksi

for a in set_movser:
    
    counter+=1
    counter2+=1
    print("Extracting " + str(counter)+ " of " + str(len(set_movser)) + " data", end='\r')

    # Get Response From iflix.com
    link = "https://www.iflix.com" + a
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    a = str(soup.find(type="application/ld+json").string)
    obj = json.loads(a)
    a = obj['@graph'][0]
    tipe = a['@type']

    #Ekstrak data dari <body> (hanya untuk Movies & TVSeries)
    if(str(tipe)!="Clip" and str(tipe)!="Corporation" and link not in set_error):
        tag = soup.find_all('div')[15]
        judul = tag.find('h1').string
        content_tipe = tag.find_all('li')[0].string
        tahun = tag.find_all('li')[1].string
        genre2 = tag.find_all('span')[1]
        genre1 = genre2.find_all('a')
        genre = []
        for i in genre1 :
            genre.append(i.string)

        ctr = 0
        valid = 0
        tag1 = soup.find_all('div')[19]


        subtitle = []
        subtitles = tag1.find_all('span')[0]
        if ("Subtitle" in str(subtitles)):
            a = subtitles.find_all('span')
            a.pop(0)
            for i in a :
                subtitle.append(i.string)
            ctr += len(a)+2
            valid +=1



        starring = []
        starrings = tag1.find_all('span')[ctr]
        if("Starring" in str(starrings)):
            b = starrings.find_all('span')
            b.pop(0)
            for i in b :
                starring.append(i.string)
            ctr += len(b) + 2


        director = []
        directors = tag1.find_all('span')[ctr]
        if("Director" in str(directors)):
            c = directors.find_all('span')
            c.pop(0)
            ctr += len(c) + 2
            for i in c :
                director.append(i.string)


        synopsiss = tag1.find_all('span')[ctr]
        if (valid==1):
            synopsis = synopsiss.find_all('span')[2].string
        else:
            synopsis = synopsiss.string

        if(synopsis == None):
            synopsis = synopsiss.find_all('span')[2].string



    #Ektraksi Data dari <head> (untuk Movies, TVSeries, Clip)
    a = str(soup.find(type="application/ld+json").string)
    obj = json.loads(a)
    

    a = obj['@graph'][0]
    tipe = a['@type']
    if(str(tipe)=="Movie"):

        idfilm = a['@id']
        dateCreated = a['dateCreated']
        duration = a['duration']
        image = a['image']

        b = a['potentialAction'][0]['actionAccessibilityRequirement']
        availabilityEnds = b['availabilityEnds']
        availabilityStarts = b['availabilityStarts']
        accessCategory = b['category']

        eligibleRegion = []
        for i in b['eligibleRegion']:
            eligibleRegion.append(i['name'])

        c = a['potentialAction'][0]['target']['actionPlatform']
        actionPlatform = []
        for i in c:
            actionPlatform.append(getID(i))


        data['Movie'].append({
            'id' : getID(idfilm),
            'url' : idfilm,
            'type': tipe,
            'title' : judul,
            'contentType' : content_tipe,
            'year' : tahun,
            'duration' : duration,
            'synopsis' : synopsis,
            'dateCreated' : dateCreated,
            'image' : image,
            'availabilityStarts': availabilityStarts,
            'availabilityEnds': availabilityEnds,
            'accessCategory': accessCategory,
        })

        try:
            bestRating = a['aggregateRating']['bestRating']
            ratingCount = a['aggregateRating']['ratingCount']
            ratingValue = a['aggregateRating']['ratingValue']

            data['Movie'][ctr_movies]['bestRating'] = bestRating
            data['Movie'][ctr_movies]['ratingCount'] = ratingCount
            data['Movie'][ctr_movies]['ratingValue'] = ratingValue
        except:
            data['Movie'][ctr_movies]['bestRating'] = "null"
            data['Movie'][ctr_movies]['ratingCount'] = "null"
            data['Movie'][ctr_movies]['ratingValue'] = "null"
                
        
        inputListToData('Movie',ctr_movies,'genre','name',genre)
        inputListToData('Movie',ctr_movies,'subtitle','language',subtitle)
        inputListToData('Movie',ctr_movies,'starring','actor',starring)
        inputListToData('Movie',ctr_movies,'director','director',director)
        inputListToData('Movie',ctr_movies,'eligibleRegion','region',eligibleRegion)
        inputListToData('Movie',ctr_movies,'actionPlatform','platform',actionPlatform)

        ctr_movies+=1

    elif(str(tipe)=="TVSeries"):
        idfilm = a['@id']

        b = a['containsSeason']

        seasons = []

        for i in range(len(a['containsSeason'])):
            seasons.append([])
            seasons[i].append(b[i]['@type']) #seasonType
            seasons[i].append(b[i]['dateCreated']) #dateCreated
            seasons[i].append(b[i]['name']) #name
            seasons[i].append(b[i]['numberOfEpisodes']) #numberOfEpisodes

        image = a['image']

        c = a['potentialAction'][0]['actionAccessibilityRequirement']
        availabilityEnds = c['availabilityEnds']
        availabilityStarts = c['availabilityStarts']
        accessCategory = c['category']

        eligibleRegion = []
        for i in c['eligibleRegion']:
            eligibleRegion.append(i['name'])

        d = a['potentialAction'][0]['target']['actionPlatform']
        actionPlatform = []
        for i in d:
            actionPlatform.append(getID(i))

        data['TVSeries'].append({
            'url' : idfilm,
            'id': getID(idfilm),
            'type': tipe,
            'title' : judul,
            'contentType' : content_tipe,
            'year' : tahun,
            'synopsis' : synopsis,
            'image' : image,
            'availabilityStarts': availabilityStarts,
            'availabilityEnds': availabilityEnds,
            'accessCategory': accessCategory,
        })
        
        try:
            bestRating = a['aggregateRating']['bestRating']
            ratingCount = a['aggregateRating']['ratingCount']
            ratingValue = a['aggregateRating']['ratingValue']

            data['TVSeries'][ctr_tvseries]['bestRating'] = bestRating
            data['TVSeries'][ctr_tvseries]['ratingCount'] = ratingCount
            data['TVSeries'][ctr_tvseries]['ratingValue'] = ratingValue
        except:
            data['TVSeries'][ctr_tvseries]['bestRating'] = "null"
            data['TVSeries'][ctr_tvseries]['ratingCount'] = "null"
            data['TVSeries'][ctr_tvseries]['ratingValue'] = "null"

        inputListToData('TVSeries',ctr_tvseries,'genre','name',genre)
        inputListToData('TVSeries',ctr_tvseries,'subtitle','language',subtitle)
        inputListToData('TVSeries',ctr_tvseries,'starring','actor',starring)
        inputListToData('TVSeries',ctr_tvseries,'director','director',director)
        inputListToData('TVSeries',ctr_tvseries,'seasons','season',seasons)
        inputListToData('TVSeries',ctr_tvseries,'eligibleRegion','region',eligibleRegion)
        inputListToData('TVSeries',ctr_tvseries,'actionPlatform','platform',actionPlatform)


        ctr_tvseries+=1
    
    elif(str(tipe)=="Clip"):
        description = a['description']
        image = a['image']
        name = a['name']

        data['Clip'].append({
            'id' : getID(link),
            'url': link,
            'type': tipe,
            'description': description,
            'image' : image,
            'title' :name 
        })
    else:
        #Apabila data bukan Movies, TVSeries, atau Clip maka tidak dimasukkan
        counter2-=1


print("")
print(str(counter2) + " data succesfully extracted")

## Memasukkan data ke dalam file json
with open(fileName, 'w') as outfile:
    json.dump(data, outfile,indent="\t")

print('Data succesfully saved on ' + str(fileName))

