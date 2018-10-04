#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:08:09 2018

@author: LouiseP
"""
#EX 1
#import zeep
#
#wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
#client = zeep.Client(wsdl=wsdl)
#print(client.service.ListOfCountryNamesByCode())
#print(client.service.CountryISOCode("Netherlands"))


##EX 2
import requests
import json
from pandas import DataFrame as df
import os

class Request:
    def __init__(self,url):
        self.url=url
        
    def _get_issues_to_csv(self):
        r=requests.get(self.url)
        data=json.loads(r.content)
        liste_title=[]
        liste_username=[]
        liste_labelname=[]
        
        for i in data:
            liste_title.append(i["title"])
            index=liste_title.index(i["title"])
            liste_username.append(i["user"]["login"])
            liste_int=[]
            for el in i["labels"]:   
                liste_int.append(el["name"])
            liste_labelname.insert(index,liste_int)
            
        dataframe=df({'Title of issue':liste_title, 'Username':liste_username, 'Names of label':liste_labelname})
        dataframe.to_csv('CSV/list_issues.csv',sep='\t')
        
        
    def _get_number_of_issues(self):
        r=requests.get(self.url)
        data=json.loads(r.content)
        return len(data)

#Fonction utile pour créer des dossiers
def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
#création d'un dossier CSV ou stocker quelques vues csv des employés
makemydir('CSV')    

url="https://api.github.com/repos/epoberezkin/ajv/issues"
req =Request(url)
req._get_issues_to_csv()
print(req._get_number_of_issues())


#headers={'Content-Type':'application/vnd.github.symmetra-preview+json'
   #     }




