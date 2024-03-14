import requests
from bs4 import BeautifulSoup


class VarleScrapper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print('Something went wrong cannot get a website data..')

    def parse_page(self):
        product = self.soup.find_all('div', class_='GRID_ITEM')
        for product in products:
            product_name = product.find('div', class_='product_title').text.strip()
            print(f"Produkto pavadinimas: {product_name}")


    def run(self):
        self.fetch()
        if self.soup:
            self.parse_page()


scraper = VarleScrapper('https://www.varle.lt/isoriniai-kietieji-diskai-hdd/')
scraper.run()