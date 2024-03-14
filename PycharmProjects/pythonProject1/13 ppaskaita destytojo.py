import requests
from bs4 import BeautifulSoup

#
# class VarleScraper:
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
#         product_list = []
#         products = self.soup.find_all('div', class_='GRID_ITEM')
#         for product in products:
#             product_name = product.find('div', class_='product-title').text.strip()
#             product_price = product.find('span', class_='price-value').text.strip().replace('\n\xa0','')
#             rating = product.find('li', attrs={'class': 'rating'}).text.strip().replace('\n(127)', '')[:3]
#             #print(f"Produkto pavadinimas: {len(product_name)}")
#
#             product_list.append({
#                 'Produkto pavadinimas': product_name,
#                 'Produkto kaina': product_price,
#                 'Ivertinimas': rating
#             })
#         print(product_list)
#     def run(self):
#         self.fetch()
#         if self.soup:
#             self.parse_page()
#
#
# scraper = VarleScraper('https://www.varle.lt/isoriniai-kietieji-diskai-hdd/')
# scraper.run()

import requests
from bs4 import BeautifulSoup


# class VarleScraper:
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
#         product_list = []
#         products = self.soup.find_all('div', class_='GRID_ITEM')
#         for product in products:
#             product_name = product.find('div', class_='product-title').text.strip()
#             product_price = product.find('span', class_='price-value').text.strip().replace('\n\xa0', '')
#             rating = product.find('li', attrs={'class': 'rating'}).text.strip().replace('\n', '')[:3]
#
#             # print(product_price)
#             product_list.append({
#                 'Produkto pavadinimas': product_name,
#                 'Produkto kaina': product_price,
#                 'Ivertinimas': rating
#             })
#         print(product_list)
#
#     def run(self):
#         self.fetch()
#         if self.soup:
#             self.parse_page()
#
#
# scraper = VarleScraper('https://www.varle.lt/isoriniai-kietieji-diskai-hdd/')
# scraper.run()

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = []
    products = soup.find_all('div', {'class': 'GRID_ITEM'})
    for product in products:
        product_name = product.find('div', class_='product-title').text.strip()
        product_price = product.find('span', class_='price-value').text.strip()

        product_list.append({
            'Produkto pavadinimas': product_name,
            'Produkto kaina': product_price
        })
    print(product_list)


def scrape_page():
    url = "https://www.varle.lt/isoriniai-kietieji-diskai-hdd/"
    html = fetch_page(url)
    if html:
        parse_page(html)
    else:
        print("Failed to retrieve page")


scrape_page()

React

Reply



import requests
from bs4 import BeautifulSoup


# class VarleScraper:
#     def __init__(self, url):
#         self.url = url
#         self.soup = None
#
#     def fetch(url):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#         else:
#             print('Something went wrong cannot get a website data..')
#
#     def parse_page(self):
#         product_list = []
#         products = self.soup.find_all('div', class_='GRID_ITEM')
#         for product in products:
#             product_name = product.find('div', class_='product-title').text.strip()
#             product_price = product.find('span', class_='price-value').text.strip().replace('\n\xa0', '')
#             rating = product.find('li', attrs={'class': 'rating'}).text.strip().replace('\n', '')[:3]
#
#             # print(product_price)
#             product_list.append({
#                 'Produkto pavadinimas': product_name,
#                 'Produkto kaina': product_price,
#                 'Ivertinimas': rating
#             })
#         print(product_list)
#
#     def run(self):
#         self.fetch()
#         if self.soup:
#             self.parse_page()
#
#
# scraper = VarleScraper('https://www.varle.lt/isoriniai-kietieji-diskai-hdd/')
# scraper.run()

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = []
    products = soup.find_all('div', {'class': 'GRID_ITEM'})
    for product in products:
        product_name = product.find('div', class_='product-title').text.strip()
        product_price = product.find('span', class_='price-value').text.strip()

        product_list.append({
            'Produkto pavadinimas': product_name,
            'Produkto kaina': product_price
        })
    return product_list


def scrape_page(base_url, start_page=1, max_pages=5):
    # varle.lt/isoriniai-kietieji-diskai-hdd/?p=3
    all_products = []
    current_page = start_page
    while current_page <= max_pages:
        url = f"{base_url}?p={current_page}"
        print(f"Scraping page {url}")
        html = fetch_page(url)
        if html:
            has_products = parse_page(html)
            if has_products:
                all_products.extend(has_products)
            else:
                print("No more products found! Stopping..")
                break
        else:
            print("Failed to retrieve page!")
            break
        current_page += 1
    print(f"Total products: {len(all_products)}")
    for product in all_products:
        print(product)


base_url = "https://www.varle.lt/isoriniai-kietieji-diskai-hdd/"
scrape_page(base_url)

