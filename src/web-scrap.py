import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json

        


#data
data = []
def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)

def clearResult(kata):
    sub = {'\u2013':'-','\u00a0':' ','\u00b7':'','\u2019':'\'','\u201c':'' }
    return replace(kata,sub)
def scrapData(soup):
    data = []
    for job in soup.find_all('div', attrs={"class" : "jobs-data featured-"}):
        jobObj = {
            "jobTitle" : clearResult(job.find('h2').text.strip()),
            "jobType" : clearResult(job.find('i', attrs={"class" : "job-type"}).text.strip()),
            "jobDesc" : clearResult(job.find('p').text.strip())
        }
        data.append(jobObj)
    return data
        
        
#scraping-laman
result = []
pages = ['1','2','3','4','5','6']
for noPage in pages:
    if( noPage == '1'):
        url = 'http://studentjob.co.id/?s=web+dev&category_name=part-time'
        response = requests.get(url,timeout = 5)
        soup = BeautifulSoup(response.content,'html.parser')
        result.append(scrapData(soup))
    else:
        url = 'http://studentjob.co.id/index.php/page/'+noPage + '/?s=web+dev&category_name=part-time'
        response = requests.get(url,timeout = 5)
        soup = BeautifulSoup(response.content,"html.parser")
        result.append(scrapData(soup))

for i in result:
    for j in i:
        data.append(j)
        
#Json
with open('..\\data\\parttime.json', 'w') as outfile:
    json.dump(data,outfile)
        