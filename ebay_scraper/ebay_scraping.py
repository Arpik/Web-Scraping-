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

def get_detail_data(soup):
    #title
    #price
    #sold

# main() function will manage the calls of other functions and will collect scraped data.
def main():
    url = 'https://www.ebay.com/itm/Kids-Beginner-Snowboard-Snow-Skis-and-Poles-with-Bindings-Set-Age-5-10-Portable/254005066272?_trkparms=ispr%3D1&hash=item3b23e1ba20:m:mZC53R_FD2jF9LFmanfxP5w&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qVB83It1FxuBslqVpLk28NGWJ8mQ4%2FdkPhzUFfvR9hzA9ehzJz3sPlNXanftxuWBNVYUAP3Hd65%2F1rrJzQcNNL0Yz6nQk97GmF1FZx4KY5jslzIGExMVQJ9YcljL1AuD2A1n13Ou9DDUsOI0j9NyD2rkDmXGmxzpITnzMZQw%2BhdjGsKn2EZkZH9h9qVdCFE%2BLPJ24qOiQx%2Bky2zw4cMsY4JB1HjkLTVwFKlzIDg3ihgGzgzkERUml%2FzCmS%2F05pclStHPHQG2FXqMdoq%2FiL2Cvv%2BchFc2yMq%2Bb84NwI%2BfUPAxJxjKcO0NZaeTwlZJxBOIOGxQMGq%2BProgdBAbStN3MbGOO1tCxQR2sqgyJfSuNrfboM%2Fs1JO%2BJGTZTWPLeDAHnm%2Ft8bv7kre0U2ozgtS1YcE6R5ddSbvhsn%2BScWk5p0L0pfNBL5RjgOWJM%2FhHI6wIOEmUcW9aJSCowIXK4YsMTF2e3kg4p4iCx0kVM8W6oDzoQWPNTIJDAM3QqeRpWkz08xo0injw5RrTbljsDT%2B5cW9ckyPNgRfBBnmJ7f1rGXGaqiWBZek8vdTQzfoBTjbLw1BhCIicxjNa7wyHlTW4xQeVaRrX9VJgbLehC6O3fSk%2FQ421BN6nq9zGNWNA5CCLAiu7jwBE5qWua%2FZt0KIu9T809VrT7qD6HbyfGJ14O8xMm9p6j5DUu5LZF2ivZVRuRoFKK3FZ5IdUuiWoXO%2F3pqAN1jtlJWxZP1g7DUgYdhAxg%3D%3D&checksum=254005066272a3b1fa6e62c44e56a7eb9be043886d0d&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qVB83It1FxuBslqVpLk28NGWJ8mQ4%2FdkPhzUFfvR9hzA9ehzJz3sPlNXanftxuWBNVYUAP3Hd65%2F1rrJzQcNNL0Yz6nQk97GmF1FZx4KY5jslzIGExMVQJ9YcljL1AuD2A1n13Ou9DDUsOI0j9NyD2rkDmXGmxzpITnzMZQw%2BhdjGsKn2EZkZH9h9qVdCFE%2BLPJ24qOiQx%2Bky2zw4cMsY4JB1HjkLTVwFKlzIDg3ihgGzgzkERUml%2FzCmS%2F05pclStHPHQG2FXqMdoq%2FiL2Cvv%2BchFc2yMq%2Bb84NwI%2BfUPAxJxjKcO0NZaeTwlZJxBOIOGxQMGq%2BProgdBAbStN3MbGOO1tCxQR2sqgyJfSuNrfboM%2Fs1JO%2BJGTZTWPLeDAHnm%2Ft8bv7kre0U2ozgtS1YcE6R5ddSbvhsn%2BScWk5p0L0pfNBL5RjgOWJM%2FhHI6wIOEmUcW9aJSCowIXK4YsMTF2e3kg4p4iCx0kVM8W6oDzoQWPNTIJDAM3QqeRpWkz08xo0injw5RrTbljsDT%2B5cW9ckyPNgRfBBnmJ7f1rGXGaqiWBZek8vdTQzfoBTjbLw1BhCIicxjNa7wyHlTW4xQeVaRrX9VJgbLehC6O3fSk%2FQ421BN6nq9zGNWNA5CCLAiu7jwBE5qWua%2FZt0KIu9T809VrT7qD6HbyfGJ14O8xMm9p6j5DUu5LZF2ivZVRuRoFKK3FZ5IdUuiWoXO%2F3pqAN1jtlJWxZP1g7DUgYdhAxg%3D%3D&checksum=254005066272a3b1fa6e62c44e56a7eb9be043886d0d'
    get_page(url)

# Checks if ebay_scraping.py was run directly from the console or not.
if __name__ = '__main__':
    main()
