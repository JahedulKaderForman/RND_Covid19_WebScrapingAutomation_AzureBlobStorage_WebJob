#!pip install requests-html

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

print("start covitNinty Web Scraping...........")

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

from datetime import date
import uuid
today = date.today()
coronaFileName="WorldWideCovidNinty.csv"
AllCountryCoronainfoCSV = df.to_csv (index_label="idx", encoding = "utf-8")

BdCoronaInfo="BagnadeshCovidNinty.csv"
BdCoronaInfoCsv= BdDataFrame.to_csv (index_label="idx", encoding = "utf-8")

TotalCoronaInfo="TotalCovidNinty.csv"
TotalCoronaInfoCsv= TotalCoronaDataFrame.to_csv (index_label="idx", encoding = "utf-8")

#!pip install azure-storage-blob==0.37.1

#block_blob_service.create_container('mycontainer')

from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

block_blob_service = BlockBlobService(account_name='', account_key='')

#Upload the CSV file to Azure blob cloud
block_blob_service .create_blob_from_text('mycontainer', coronaFileName, AllCountryCoronainfoCSV)
block_blob_service .create_blob_from_text('mycontainer', BdCoronaInfo, BdCoronaInfoCsv)
block_blob_service .create_blob_from_text('mycontainer', TotalCoronaInfo, TotalCoronaInfoCsv)

print("Successfully end covitNinty Web Scraping...........")

