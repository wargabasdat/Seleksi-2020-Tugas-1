import bs4, re, csv, requests, json
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36', 
    'From': 'fakhrurridawidodo@gmail.com'
}

# Fungsi untuk "membersihkan" nama pemain dari " FIFA 20"
def removeFIFA(aString):
    return aString.replace(' FIFA 20','')

# Sebuah fungsi yang mengembalikan data "mentah" dari sebuah page dengan tool "Selenium Webdriver"
def openUrlSelenium(url):
    driver = 14
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    driver.close()
    return soup

# Sebuah fungsi yang mengembalikan data "mentah" dari sebuah page
def openUrl(url):
    result = requests.get(url)
    html = result.content   
    soup = BeautifulSoup(html,'lxml')
    return soup

# Mengcollect HANYA url dari tiap pemain pada web fifaindex.com/players/<page_number>
def scrapeLuar(soup):
    all_tables = soup.find_all('tr')
    i=1
    nameList = []
    urlList = []
    for table in all_tables:
        playerData = table.find("td")
        if(playerData!=None):
            a = playerData.find("a")
            if(a!=None):
                urlList.append("https://www.fifaindex.com" + a["href"])
    return urlList
    
# Mengambil HANYA url dari seluruh pemain yang terdaftar pada web fifaindex.com
# untuk kemudian disimpan dalam sebuah file csv dengan nama 'Urls.csv'
def collectPlayerUrl():
    url = 'https://www.fifaindex.com'
    for i in range(1,657):
        print("Processing page ", i, "...")
        url_temp = url+'/players/'+str(i)+'/'
        soup = openUrl(url_temp)
        B = scrapeLuar(soup)
        df=pd.DataFrame({'url' : B})
        df.to_csv('Urls.csv', mode='a', index = False, header = False, encoding = 'utf-8')

# Melakukan scraping data per pemain dari url(s) yang telah diperoleh dari prosedur scrapeLuar
def scrapeDalamToCSV(url):
    soupDalam = openUrl(url)
    player_name = ambilNama(soupDalam)
    print("Processing the page of ",player_name[0])
    player_rating = ambilRating(soupDalam)
    player_club = ambilKlub(soupDalam)
    player_nation = ambilNegara(soupDalam)
    player_wf = ambilWeakFootRt(soupDalam)
    player_sm = ambilSkillMovesRt(soupDalam)
    player_position = ambilPosition(soupDalam)
    player_stats = ambilPersonalStats(soupDalam)
    height = re.sub("[^0-9]", "", player_stats[0])
    weight = re.sub("[^0-9]", "", player_stats[1])
    df = pd.DataFrame({'name':player_name, 'ovr':player_rating[0], 'pot':player_rating[1], 'nationality': player_nation, 'club': player_club, 'weak_foot_rating': player_wf, 'skill_moves_rating': player_sm, 'club_position': player_position, 'height': int(height), 'weight': int(weight),'foot_preference': player_stats[2], 'birth_date': player_stats[3], 'age': int(player_stats[4]),'work_rate': player_stats[5], 'value': player_stats[6], 'wage': player_stats[7], 'ball_control': int(player_stats[11]), 'dribbling': int(player_stats[12]), 'marking': int(player_stats[13]), 'slide_tackle': int(player_stats[14]), 'stand_tackle': int(player_stats[15]), 'aggression': int(player_stats[16]), 'reactions': int(player_stats[17]), 'att_position': int(player_stats[18]), 'interceptions': int(player_stats[19]), 'vision': int(player_stats[20]), 'composure': int(player_stats[21]), 'crossing': int(player_stats[22]), 'short_pass': int(player_stats[23]), 'long_pass': int(player_stats[24]), 'acceleration': int(player_stats[25]), 'stamina': int(player_stats[26]), 'strength': int(player_stats[27]), 'balance': int(player_stats[28]), 'sprint_speed': int(player_stats[29]), 'agility': int(player_stats[30]), 'jumping': int(player_stats[31]), 'heading': int(player_stats[32]), 'shot_power': int(player_stats[33]), 'finishing': int(player_stats[34]), 'long_shots': int(player_stats[35]), 'curve': int(player_stats[36]), 'fk_acc': int(player_stats[37]), 'penalties': int(player_stats[38]), 'volleys': int(player_stats[39]),  'gk_positioning': int(player_stats[40]), 'gk_diving': int(player_stats[41]), 'gk_handling': int(player_stats[42]), 'gk_kicking': int(player_stats[43]), 'gk_reflexes': int(player_stats[44])})
    df.to_csv('FIFA_index_20.csv', mode='a', index = True, header = False, encoding = 'utf-8')

# Melakukan scraping data per pemain dari url(s) yang telah diperoleh dari prosedur scrapeLuar dengan menambahkan header
def firstScrapeDalamToCSV(url):
    soupDalam = openUrl(url)
    player_name = ambilNama(soupDalam)
    print("Processing the page of ",player_name[0])
    player_rating = ambilRating(soupDalam)
    player_club = ambilKlub(soupDalam)
    player_nation = ambilNegara(soupDalam)
    player_wf = ambilWeakFootRt(soupDalam)
    player_sm = ambilSkillMovesRt(soupDalam)
    player_position = ambilPosition(soupDalam)
    player_stats = ambilPersonalStats(soupDalam)
    height = re.sub("[^0-9]", "", player_stats[0])
    weight = re.sub("[^0-9]", "", player_stats[1])
    df = pd.DataFrame({'name':player_name, 'ovr':player_rating[0], 'pot':player_rating[1], 'nationality': player_nation, 'club': player_club, 'weak_foot_rating': player_wf, 'skill_moves_rating': player_sm, 'club_position': player_position, 'height': int(height), 'weight': int(weight),'foot_preference': player_stats[2], 'birth_date': player_stats[3], 'age': int(player_stats[4]),'work_rate': player_stats[5], 'value': player_stats[6], 'wage': player_stats[7], 'ball_control': int(player_stats[11]), 'dribbling': int(player_stats[12]), 'marking': int(player_stats[13]), 'slide_tackle': int(player_stats[14]), 'stand_tackle': int(player_stats[15]), 'aggression': int(player_stats[16]), 'reactions': int(player_stats[17]), 'att_position': int(player_stats[18]), 'interceptions': int(player_stats[19]), 'vision': int(player_stats[20]), 'composure': int(player_stats[21]), 'crossing': int(player_stats[22]), 'short_pass': int(player_stats[23]), 'long_pass': int(player_stats[24]), 'acceleration': int(player_stats[25]), 'stamina': int(player_stats[26]), 'strength': int(player_stats[27]), 'balance': int(player_stats[28]), 'sprint_speed': int(player_stats[29]), 'agility': int(player_stats[30]), 'jumping': int(player_stats[31]), 'heading': int(player_stats[32]), 'shot_power': int(player_stats[33]), 'finishing': int(player_stats[34]), 'long_shots': int(player_stats[35]), 'curve': int(player_stats[36]), 'fk_acc': int(player_stats[37]), 'penalties': int(player_stats[38]), 'volleys': int(player_stats[39]),  'gk_positioning': int(player_stats[40]), 'gk_diving': int(player_stats[41]), 'gk_handling': int(player_stats[42]), 'gk_kicking': int(player_stats[43]), 'gk_reflexes': int(player_stats[44])})
    df.to_csv('FIFA_index_20.csv', mode='a', index = True, header = True, encoding = 'utf-8')

# Mengambil nama pemain
def ambilNama(soupDalam):
    all_tables = soupDalam.find_all('div', {"class": "align-self-center pl-3"})
    nameList = []
    for table in all_tables:
        playerData = table.find("h1")
        if(playerData!=None):
            clean_name = playerData.text.replace(' FIFA 20','')
            nameList.append(clean_name)
    return nameList

# Mengambil asal negara pemain
def ambilNegara(soupDalam):
    all_tables = soupDalam.find_all('div', {"class": "align-self-center pl-3"})
    nameList = []
    for table in all_tables:
        playerData = table.find("h2")
        if(playerData!=None):
            clean_national = playerData.find("a")
            nameList.append(clean_national["title"])
    return nameList[0]

# Meng-collect statistik personal dalam urutan tinggi (cm), berat (kg), kaki, tanggal lahir
# umur, workrate, valuasi pemain (pounds), gaji per tahun (pounds), nomor punggung klub,
def ambilPersonalStats(soupDalam):
    all_tables = soupDalam.find_all('div', {"class": "card mb-5"})
    nameList = []
    # Membersihkan data trivial yang tidak diinginkan
    for divs in all_tables: 
        for div in divs.find_all("span", {"class":["data-units data-units-imperial","star"]}):
            div.decompose()
        for div in divs.find_all("p", {"class":["data-currency data-currency-dollar","data-currency data-currency-pound"]}):
            div.decompose()
        for div in divs.find_all("a", {"class":"link-position"}):
            div.decompose()
    # Mengekstrak data yang diinginkan
    for table in all_tables:
        playerData = table.find("div", {"class": "card-body"})
        if(playerData!=None):
            clean_ratings = playerData.find_all("span", {"class": "float-right"})
            for rating in clean_ratings:
                if(rating!=[]):
                    if bool(rating.text):
                        nameList.append(rating.text)
    # Untuk pemain tetap sebuah tim
    if (len(nameList)==44):
        nameList.insert(6, '€0')
        nameList.insert(7, '€0')
    if (len(nameList)==40):
        nameList.insert(6, '€0')
        nameList.insert(7, '€0')
        nameList.insert(8, '99')
        nameList.insert(9, 'January 1, 1970')
        nameList.insert(10, '1970')
    if (len(nameList)==46):
        del nameList[8]
    # Untuk pemain pinjaman dari tim lain
    elif (len(nameList)==47):
        del nameList[8]
        del nameList[9]   
    return nameList

# Mengambil posisi bermain pemain di klub
def ambilPosition(soupDalam):
    all_tables = soupDalam.find_all('p')
    positionList = []
    cleanPosition = []
    for table in all_tables:
        if ("Position " in table.get_text()):
            positionList.append(table)
    aList = positionList[0].find_all('a')
    for a in aList:
        if (a!=None):
            cleanPosition.append(a['title'])
    if len(cleanPosition)!=0:
        return cleanPosition[0]
        
# Mengambil nilai rating weak foot pemain (dalam skala 1-5)
def ambilWeakFootRt(soupDalam):
    all_tables = soupDalam.find_all('p')
    nameList = []
    for table in all_tables:
        if (table.get_text() == "Weak Foot "):
            nameList.append(table)
    return len(nameList[0].find_all('i', {"class":"fas fa-star fa-lg"}))

# Mengambil nilai rating skill moves pemain (dalam skala 1-5)
def ambilSkillMovesRt(soupDalam):
    all_tables = soupDalam.find_all('p')
    nameList = []
    for table in all_tables:
        if (table.get_text() == "Skill Moves "):
            nameList.append(table)
    return len(nameList[0].find_all('i', {"class":"fas fa-star fa-lg"}))

# Mengambil klub pemain
def ambilKlub(soupDalam):
    all_tables = soupDalam.find_all('div', {"class": "col-12 col-sm-6 col-lg-6 team"})
    nameList = []
    for table in all_tables:
        playerData = table.find_all("h5", {"class": "card-header"})
        clean_national = playerData[0].find("a")
        if(clean_national!=None):
            nameList.append(clean_national["title"])
    # [0] for country, [1] for club
    if(len(nameList)!=0):
        if len(nameList)==1:
            return removeFIFA(nameList[0])
        else:
            return removeFIFA(nameList[1])

# Mengambil nilai rating pemain (In the order of OVR & POT)
def ambilRating(soupDalam):
    all_tables = soupDalam.find_all('div', {"class": "card mb-5"})
    nameList = []
    for table in all_tables:
        playerData = table.find("h5")
        if(playerData!=None):
            clean_ratings = playerData.find_all("span", {"class": "float-right"})
            for rating in clean_ratings:
                if(rating!=[]):
                    nameList.append(int(rating.text.split()[0]))
                    nameList.append(int(rating.text.split()[1]))
    return nameList

# Melakukan scraping data pemain dengan bantuan multiprocessing.Pool
def pooledScraping(urlList):
    p = Pool()
    result = p.map(scrapeDalamToCSV, urlList)
    p.close()
    p.join()

# Menyimpan seluruh url pemain dari <filename>.csv dalam sebuah array 
# bernama url_list
def getUrlList(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        url_list = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                url_list.append(row[0])
                line_count += 1
    return url_list

# "Membersihkan" data nilai value dan wage dari karakter "€" dan mengubah menjadi
# tipe float
def cleanCurrency(csvFilename, newCsvFilename):
    df_orig = pd.read_csv(csvFilename, encoding='utf-8')
    df = df_orig.copy()
    df['value'] = df['value'].str.replace('.', '')
    df['value'] = df['value'].str.replace('€', '')
    df['wage'] = df['wage'].str.replace('.', '')
    df['wage'] = df['wage'].str.replace('€', '')
    df["value"] = pd.to_numeric(df["value"], downcast="float")
    df["wage"] = pd.to_numeric(df["wage"], downcast="float")
    df.to_csv(newCsvFilename, index=True, encoding='utf-8')

# Mengkonversi file csv hasil scraping menjadi file json
def csvToJsonFile(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            id = rows['id']
            data[id] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


if __name__ == '__main__': 
    urlList = getUrlList('Urls.csv')
    firstScrapeDalamToCSV('https://www.fifaindex.com/player/158023/lionel-messi/')
    ## For peak hours
    for url in urlList:
        scrapeDalamToCSV(url)
    ## For off-peak hours
    #pooledScraping(urlList)