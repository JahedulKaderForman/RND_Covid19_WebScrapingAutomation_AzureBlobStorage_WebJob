from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
import re
import pandas as pd

import requests
from bs4 import BeautifulSoup
URL = 'https://www.worldometers.info/coronavirus/'
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
country_table=soup.find('table', id="main_table_countries_today")
thead = country_table.findAll('thead')
theadTh = country_table.findAll('th')
Headervalues = []

#read folder location 
with open('folderLocation.txt', 'r') as file:
    folderlocation = file.read().replace('\n', '')

print('Web scraping start for downloading covid 19 data')

for th in theadTh:
  Headervalues.append(th.text)
print(Headervalues)

def cleanData(data):
  newcleanData =re.sub(r"[,+]", "", data)
  return newcleanData

CountryWiseInformation=[[],[],[],[],[],[],[],[],[]]
BangladeshCoronaInfo=[]

tbody=country_table.findAll('tbody')
indivualCoronaInfoCountry=tbody[0]
coutryAlltr = indivualCoronaInfoCountry.findAll('tr')
for countryTr in coutryAlltr:
  countryTd=countryTr.findAll('td')
  courtryName=cleanData(countryTd[0].text)
  if(courtryName=="Bangladesh"):
    BangladeshCoronaInfo.append(cleanData(countryTd[0].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[1].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[2].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[3].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[4].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[5].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[6].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[7].text))
    BangladeshCoronaInfo.append(cleanData(countryTd[8].text))

  CountryWiseInformation[0].append(cleanData(countryTd[0].text))
  CountryWiseInformation[1].append(cleanData(countryTd[1].text))
  CountryWiseInformation[2].append(cleanData(countryTd[2].text))
  CountryWiseInformation[3].append(cleanData(countryTd[3].text))
  CountryWiseInformation[4].append(cleanData(countryTd[4].text))
  CountryWiseInformation[5].append(cleanData(countryTd[5].text))
  CountryWiseInformation[6].append(cleanData(countryTd[6].text))
  CountryWiseInformation[7].append(cleanData(countryTd[7].text))
  CountryWiseInformation[8].append(cleanData(countryTd[8].text))

TotalCoronaValues=[]
TotalCoronaInfo=tbody[1]
TotalCoronaInfoTd = TotalCoronaInfo.findAll('td')
for td in TotalCoronaInfoTd:
  TotalCoronaValues.append(td.text)

data = { "Country,Other": CountryWiseInformation[0],
         "TotalCases":  CountryWiseInformation[1],
         "NewCases" : CountryWiseInformation[2],
         "TotalDeaths" :  CountryWiseInformation[3],
         "NewDeaths" : CountryWiseInformation[4],
         "TotalRecovered" :   CountryWiseInformation[5],
         "ActiveCases" : CountryWiseInformation[6],
         "Serious,Critical" :  CountryWiseInformation[7],
         "Tot\xa0Cases/1M pop" :  CountryWiseInformation[8]
        }
df = pd.DataFrame(data, columns=['Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical', 'Tot\xa0Cases/1M pop'])

print(BangladeshCoronaInfo[8])

BdData = { "Country,Other": BangladeshCoronaInfo[0],
         "TotalCases":  BangladeshCoronaInfo[1],
         "NewCases" : BangladeshCoronaInfo[2],
         "TotalDeaths" :  BangladeshCoronaInfo[3],
         "NewDeaths" : BangladeshCoronaInfo[4],
         "TotalRecovered" :   BangladeshCoronaInfo[5],
         "ActiveCases" : BangladeshCoronaInfo[6],
         "Serious,Critical" :  BangladeshCoronaInfo[7],
         "Tot\xa0Cases/1M pop" :  BangladeshCoronaInfo[8]
        }
BdDataFrame = pd.DataFrame(BdData, columns=['Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical', 'Tot\xa0Cases/1M pop'],index=[0])



TotalCoronaData = {
         "TotalCases":  TotalCoronaValues[1],
         "NewCases" : TotalCoronaValues[2],
         "TotalDeaths" :  TotalCoronaValues[3],
         "NewDeaths" : TotalCoronaValues[4],
         "TotalRecovered" :   TotalCoronaValues[5],
         "ActiveCases" : TotalCoronaValues[6],
         "Serious,Critical" :  TotalCoronaValues[7],
         "Tot\xa0Cases/1M pop" :  TotalCoronaValues[8]
        }
TotalCoronaDataFrame = pd.DataFrame(TotalCoronaData, columns=['TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical', 'Tot\xa0Cases/1M pop'],index=[0])

#download csv file 
#Allcountry info csv
df.to_csv("CoronaInfoWorldometers.csv", index=None, encoding='utf-8')

#BD corona Info csv
BdDataFrame.to_csv("BdCoronaInfo.csv", index=None, encoding='utf-8')

#Total Corona Info csv
TotalCoronaDataFrame.to_csv("TotalCoronaInfo.csv", index=None, encoding='utf-8')

import csv


from datetime import date
today = date.today()
import uuid
# save same folder start
# row_contents = [today,BangladeshCoronaInfo[1],BangladeshCoronaInfo[3]]

# from csv import writer
# todayBdCovidNinty=open("E:/RND/TotalBdCorona.csv",'w+')
# def append_list_as_row(file_name, list_of_elem):
#     # Open file in append mode
#     with open(file_name, 'a', newline='\n') as write_obj:
#         # Create a writer object from csv module
#         csv_writer = writer(write_obj)
#         # Add contents of list as last row in the csv file
#         csv_writer.writerow(list_of_elem)

# append_list_as_row("E:/RND/CoronaVsCode/TotalBdCorona.csv", row_contents)

# save same folder end


#save daily data csv in folder
coronaFileName="AllcountryCovid"+str(today)+"_id_"+str(uuid.uuid4())+".csv"
BdCoronaInfo="BangladeshCovid"+str(today)+"_id_"+str(uuid.uuid4())+".csv"
TotalCoronaInfo="TotalWorldCovid"+str(today)+"_id_"+str(uuid.uuid4())+".csv"

#Allcountry info csv
df.to_csv(folderlocation+coronaFileName, index=None, encoding='utf-8')

#BD corona Info csv
BdDataFrame.to_csv(folderlocation+BdCoronaInfo, index=None, encoding='utf-8')

#Total Corona Info csv
TotalCoronaDataFrame.to_csv(folderlocation+TotalCoronaInfo, index=None, encoding='utf-8')

print('Data Successfully Download.Check in this location : - '+folderlocation)