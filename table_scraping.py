import csv
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_pokemon_name():
    request = requests.get('https://pokemondb.net/pokedex/all')
    soup = bs4.BeautifulSoup(request.text, 'lxml')
    table = soup.find('table', {'class' : 'data-table block-wide'})
    tbody_rows = table.tbody.find_all('tr')
    pok_names = []
    for i in range(0,10): 
        pok_name = tbody_rows[i].find_all('td', {'class' : 'cell-name'})[0].find('a').text
        pok_names.append(pok_name)
    
    return pok_names

