import json
from colorama import Fore
from all_search_api import yandex
from all_search_api import google
from all_search_api import bing
from datetime import datetime
import os
import requests as r


def download_logs(logs,directory):
  try:
    text = logs.split('/')
    text = text[len(text)-1]
    if '?' in text:
      text_mass = text.split('?')
      text = text_mass[0]
    content = r.get(logs).text
    f = open(directory+'/'+text,'w')
    f.write(content)
    f.close()
    print(Fore.GREEN+'Log '+text+' downloaded and saved successfully.')
    pass
  except Exception as e:
    print(Fore.RED+'Exception: '+str(e))
    pass

def mkdir(directory):
  os.system('mkdir '+directory)

def save_results(mass,filename):
  print(mass)
  f = open(filename,'w')
  f.write(str(mass).replace("'",'"'))
  f.close()

#keywords_search = 'allintext:password filetype:log after:2019'

keywords_search = str(input('Enter google dork: '))

lol = datetime.now()
print(lol.strftime("%Y-%m-%d-%H-%M-%S"))
nowtimedate = str(lol.strftime("%Y-%m-%d-%H-%M-%S"))
mass = ['10','20','30','40']
for star in mass:
  google_search = google(keywords_search+'&start='+star)
  mkdir(nowtimedate)
  mkdir(nowtimedate+'/search')
  mkdir(nowtimedate+'/logs')
  save_results(google_search,nowtimedate+'/search/'+star+':start-google_search-'+nowtimedate+'.txt')
  start = 0
  end = len(google_search)-1
  while start<end:
    download_logs(google_search[start][0],nowtimedate+'/logs')
    start+=1