from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

knygu_sarasas = []


def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_book_urls(base_url, book_url, headers):
    soup = get_soup(book_url, headers)
    book_links = soup.find_all('div', class_='elementList')
    book_urls = [base_url + book.find('a')['href'] for book in book_links]
    return book_urls


def get_book_data(book_url, headers):
    soup = get_soup(book_url, headers)
    title = soup.find('h1').text.strip()
    author = soup.find('span', class_='ContributorLink__name').text.strip()
    raitings = soup.find('div', class_='RatingStatistics__rating').text.strip()
    kaina = soup.find('button', class_='Button Button--buy Button--medium Button--block').text.strip()
    reviews = soup.find('span', class_='u-dot-before').text.strip().replace('\xa0reviews', ' ')
    puslapiuSK = soup.find('div', class_='FeaturedDetails').text.strip().split()[0]
    pirma_priskirtaKAT = soup.find('a', class_='Button Button--tag-inline Button--small').text.strip()

    knygu_sarasas.append({'title': title, 'author': author, 'ratings': raitings, 'kaina': kaina, 'reviews': reviews,
                          'puslapiu skaicius': puslapiuSK,
                          'pirma priskirta kategorija': pirma_priskirtaKAT
                          })
    return knygu_sarasas


def main():
    base_url = 'https://www.goodreads.com/'
    book_url = 'https://www.goodreads.com/shelf/show/fiction'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}
    book_urls = get_book_urls(base_url, book_url, headers)
    for url in book_urls[:2]:
        details = get_book_data(url, headers)
        print(details)
        # df = pd.DataFrame(details)
        # df.to_csv('knygu_sarasas_test2.csv', index=False)
        sleep(1)


if __name__ == '__main__':
    main()
