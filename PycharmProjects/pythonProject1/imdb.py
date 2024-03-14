

import requests
from bs4 import BeautifulSoup
import html


def fetch(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = []
    products = soup.find_all('li', {'class': 'ipc-metadata-list-summary-item sc-1364e729-0 caNpAE cli-parent'})

    for product in products:
        product_name = product.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title').text.strip()
        product_reitingas = product.find('div', class_='sc-e2dbc1a3-0 ajrIH sc-be6f1408-2 dAeZAQ cli-ratings-container').text.strip()
        product_trukme = product.find('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item').text.strip()
        product_metai = product.find('span', class_='c-be6f1408-8 fcCUPU cli-title-metadata-item').text.strip()
        product_kategorija = product.find('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item').text.strip()

        product_list.append({
            'Pavadinimas': product_name,
            'Reitingas': product_reitingas,
            'Trukme': product_trukme,
            'Metai': product_metai,
            'Kategorija': product_kategorija

        })
    print(product_list)

def scrape_page():
    url = "https://www.imdb.com/chart/top/"
    html = fetch(url)
    if html:
        parse_page(html)
    else:
        print("Failed to retrieve page")


scrape_page()