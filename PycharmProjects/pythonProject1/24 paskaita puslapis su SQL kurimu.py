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
    print('Lentele buvo sukurta sekmingai')
    cursor.close()
    connection.close()


def gauti_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    objektai = soup.find_all('article', class_='property_block')
    for objektas in objektai:
        title = objektas.find('div', class_='title_1').text.strip()
        price = objektas.find('span', class_='price').text.strip().replace(',','.')

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
    print('Data inserted succesfully')
    cursor.close()
    connection.close()


def main():
    url = 'https://www.spainhouses.net/en/rent-flats-malaga.html'
    database_name = 'spainhouses'
    user = 'postgres'
    password = 'babilonas'
    create_database(database_name, user, password)
    data = gauti_info(url)
    create_table(database_name, user, password)
    insert_data(database_name, data, user, password)


if __name__ == '__main__':
    main()