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

def get_pokemon_links():
    request = requests.get('https://pokemondb.net/pokedex/all')
    soup = bs4.BeautifulSoup(request.text, 'lxml')
    table = soup.find('table', {'id' : 'pokedex'})
    tbody_rows = table.tbody.find_all('tr')
    pok_links = []
    for i in range(0,10): 
        pok_link = tbody_rows[i].find_all('td', class_='cell-name')[0].find('a')['href']
        pok_links.append(pok_link)

    print(pok_links)
    return pok_links

def get_pokemon_power(url):
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.text, 'lxml')
    table = soup.find('table', {'class' : 'data-table'})
    tbody_rows = table.tbody.find_all('tr')
    pok_powers = []
    for i in range(len(tbody_rows)):
        pok_power = tbody_rows[i].find_all('td', class_='cell-num')[1].text
        if pok_power == '—':
            pok_power = 0
        else:
            pok_power = int(pok_power)
        pok_powers.append(pok_power)
    return sum(pok_powers)

pokemones = get_pokemon_name()
poklinks = get_pokemon_links()

for i in range(len(poklinks)):
    poklinks[i] = 'https://pokemondb.net' + poklinks[i]


def get_powersum():
    powersum = []
    for link in poklinks:
        powersum.append(get_pokemon_power(link))
    return powersum