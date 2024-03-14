

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta




class Valiutos:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print("Error fetching..")

    def parse(self):
        table_data = []
        table = self.soup.find('table', class_='table')
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            row_data = [col.text.strip() for col in columns]
            if row_data:
                table_data.append(row_data)
        if table_data:
            df = pd.DataFrame(table_data[1:],
                              columns=['Valiutos pavadinimas', 'Valiutos kodas', 'Santykis', 'Pokytis vnt.', 'Pokytis %'])
            print(df.to_csv('VALIUTOSdata.csv', index=False))
        else:
            print("No data")

    def run(self):
        self.fetch()
        if self.soup:
            self.parse()


scraper = Valiutos('https://www.lb.lt/lt/kasdien-skelbiami-euro-ir-uzsienio-valiutu-santykiai-skelbia-europos'
                          '-centrinis-bankas?class=Eu&type=day&selected_curr=&date_day=2024-03-01')
scraper.run()

