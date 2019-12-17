# TODO
# 1. Make a request to the ebay.com.
# 2. Collect data from each detail page.
# 3. Collect all links to detail pages of each product. 
# 4. Write scraped data to a csv file.
import requests


# Make a request to a page.
def get_page(url):
    response = requests.get(url)

# main() function will manage the calls of other functions and will collect scraped data.
def main():
    pass


# Checks if ebay_scraping.py was run directly from the console or not.
if __name__ = '__main__':
    main()
