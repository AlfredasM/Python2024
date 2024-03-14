


import requests
from bs4 import BeautifulSoup

#https://spain-real.estate/property/andalusia/sevilla/


def fetch(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = []
    products = soup.find_all('li', {'data-object': True})
    for product in products:
        product_name = product.find('div', class_='title').text.strip()
        product_price = product.find('span', class_='price js-list-for-show')
        product_bedrooms = product.find('span', class_='bedrooms')
        product_bathroom = product.find('span', class_='bathrooms')
        product_livingSpace = product.find('span', class_='area')



    if product_price:
        product_price = product_price.text.strip()
    else:
        print("Informacijos nera")

    if product_bedrooms:
        product_bedrooms = product_bedrooms.text.strip()
    else:
        print("Informacijos nera")

    if product_bathroom:
        product_bathroom = product_bathroom.text.strip()
    else:
        print("Informacijos nera")

    if product_livingSpace:
        product_livingSpace = product_livingSpace.text.strip()
    else:
        print("Informacijos nera")

    product_list.append({
            'Apartamentu pavadinimas': product_name,
            'Apartamentu kaina': product_price,
            'Miegamu kambariu kiekis': product_bedrooms,
            'Vonios kambariu kiekis': product_bathroom,
            'Apartamentu plotas': product_livingSpace


        })
    print(product_list)

def scrape_page():
    url = "https://spain-real.estate/property/andalusia/sevilla/"
    html = fetch(url)
    if html:
        parse_page(html)
    else:
        print("Failed to retrieve page")

scrape_page()



