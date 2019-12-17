# TODO
# 1. Make a request to the ebay.com.
# 2. Collect data from each detail page.
# 3. Collect all links to detail pages of each product. 
# 4. Write scraped data to a csv file.
import requests
import bs4 import BeautifulSoup


# Make a request to a page.
def get_page(url):
    response = requests.get(url)   
    # Check if request was successful 
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        # Create BeautifulSoup object if request was successful.
        soup = BeautifulSoup(rewponse.text, 'lxml')
    return soup

# main() function will manage the calls of other functions and will collect scraped data.
def main():
    pass


# Checks if ebay_scraping.py was run directly from the console or not.
if __name__ = '__main__':
    main()
