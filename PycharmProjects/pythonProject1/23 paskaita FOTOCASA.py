import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(database_name, user, password):
    connection = psycopg2.connect(
        dbname='postgres',
        user=user,
        password=password,
        host='localhost'
    )

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(database_name)))
    cursor.close()
    connection.close()


def create_table(database_name, user, password):
    connection = psycopg2.connect(
        dbname=database_name,
        user=user,
        password=password,
        host='localhost'
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS houses(
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    price decimal(10, 3))
    """)
    connection.commit()
    print('Lentele sukurta sekmingai')
    cursor.close()
    connection.close()


def gauti_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    objektai = soup.find_all('article', class_='re-CardPackPremium')
    for objektas in objektai:
        title = objektas.find('span', class_='re-CardTitle').text.strip()
        price = objektas.find('span', class_='re-CardPrice').text.strip().replace(' € /month', ' ')

        data.append({
            'title': title,
            'price': price
        })
    return data


def insert_data(database_name, data, user, password):
    connection = psycopg2.connect(
        database=database_name,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    for house in data:
        cursor.execute('INSERT INTO houses (title, price) VALUES (%s, %s)', (house['title'], house['price']))
    connection.commit()
    print('Data insert succsesfully')
    cursor.close()
    connection.close()


def main():
    url = 'https://www.fotocasa.es/en/rental/homes/malaga-province/all-zones/l'
    database_name = 'fotocasahauses'
    user = 'postgres'
    password = 'babilonas'
    #create_database(database_name, user, password)
    data = gauti_info(url)
    create_table(database_name, user, password)
    insert_data(database_name, data, user, password)
    print(data)
if __name__ == '__main__':
    main()
