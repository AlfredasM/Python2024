from time import sleep

import requests
from bs4 import BeautifulSoup


def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_movie_urls(base_url, top_movie_url, headers):
    soup = get_soup(top_movie_url, headers)
    movie_links = soup.find_all('li', class_='ipc-metadata-list-summary-item')
    movie_urls = [base_url + movie.find('a')['href'] for movie in movie_links]
    return movie_urls


def get_movie_data(movie_url, headers):
    soup = get_soup(movie_url, headers)
    title = soup.find('h1').text.strip()
    genre = soup.find('span', class_='ipc-chip__text').text.strip()

    return {'url': movie_url, 'title': title, 'genre': genre}


def main():
    base_url = 'https://www.imdb.com/'
    top_movies_url = 'https://www.imdb.com/chart/top/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}
    movie_urls = get_movie_urls(base_url, top_movies_url, headers)
    for url in movie_urls[:5]:
        details = get_movie_data(url, headers)
        print(details)
        sleep(1)


if __name__ == '__main__':
    main()