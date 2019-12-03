#  Scrape a web site and download .txt 
#  files. 

import requests
import urllib.request
import time
import lxml
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "lxml")
soup.find_all('a')

txt_div = soup.find_all('div', { 'class' : 'span-84 last' })[0]
