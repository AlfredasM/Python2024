# class EstateScrapper:
#     def __init__(self, url):
#         self.url = url
#         self.soup = None
#
#     def fetch(self):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
#         response = requests.get(self.url, headers=headers)
#         if response.status_code == 200:
#             self.soup = BeautifulSoup(response.text, 'html.parser')
#         else:
#             print('Something went wrong cannot get a website data..')
#
#     def parse_page(self):
#         product = self.soup.find_all('div', class_='GRID_ITEM')
#         for product in products:
#             product_name = product.find('div', class_='product_title').text.strip()
#             print(f"Produkto pavadinimas: {product_name}")
#
#
#     def run(self):
#         self.fetch()
#         if self.soup:
#             self.parse_page()
#
#
# scraper = VarleScrapper('https://spain-real.estate/property/andalusia/sevilla/page/1/#objects')
# scraper.run()

import requests
from bs4 import BeautifulSoup




# def parse_page(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     product_list = []
#     products = soup.find_all('div', {'class', 'ipc-metadata-list-summary-item__c'})
#     for product in products:
#         product_name = product.find('h3', class_='ipc-title__text').text.strip()
#         product_reitingas = product.find('span', class_='ipc-rating-star--rate').text.strip()
#         product_trukme = product.find('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item').text.strip()
#         product_metai = product.find('span', class_='c-be6f1408-8 fcCUPU cli-title-metadata-item').text.strip()
#         product_kategorija = product.find('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item').text.strip()
#
#         product_list.append({
#             'Pavadinimas': product_name,
#             'Reitingas': product_reitingas,
#             'Trukme': product_trukme,
#             'Metai': product_metai,
#             'Kategorija': product_kategorija
#
#
#         })
#     print(product_list)
#
# def scrape_page():
#     url = "https://www.imdb.com/chart/top/"
#     html = fetch(url)
#     if html:
#         parse_page(html)
#     else: