# TODO
# 1. Make a request to the ebay.com.
# 2. Collect data from each detail page.
# 3. Collect all links to detail pages of each product. 
# 4. Write scraped data to a csv file.
import requests
from bs4 import BeautifulSoup


# Make a request to a page.
def get_page(url):
    response = requests.get(url)   
    # Check if request was successful 
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        # Create BeautifulSoup object if request was successful.
        soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_detail_data(soup): 
    
    # Get title
    try:
        title = soup.find('h1', id='itemTitle').contents[1]
    except:
        title = ''

    # Get price
    try:
        # Using .strip() to get rid of space.
        # Using .split() to split the string by space.
        p = soup.find('span', id='mm-saleDscPrc').text.strip()
        currency, price = p.split(' ')
    except:
        currency = ''
        price = ''

    # Get sold
    try:
        sold = soup.find('span', class_ = 'vi-qtyS').text.strip().split(' ')[0]
    except:
        sold = ''
    print(sold)

    # Pack all the scraped data to a dictionary
    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'total sold': sold
    }

    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_ = 's-item__link')
    except:
        links = []
    # Get all hrefs from the links list
    urls = [item.get('href') for item in links]
    
    return urls

# main() function will manage the calls of other functions and will collect scraped data.
def main():
    url = 'https://www.ebay.com/sch/i.html?&_nkw=skis&_pgn=1'
    get_page(url)

    get_index_data(get_page(url))

# Checks if ebay_scraping.py was run directly from the console or not.
if __name__ == '__main__':
    main()
