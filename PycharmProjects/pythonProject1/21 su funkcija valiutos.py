import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

def banko_duomenu_gavimas (pradzios_data, dienu_skaicius):
    base_url = ('https://www.lb.lt/lt/kasdien-skelbiami-euro-ir-uzsienio-valiutu-santykiai-skelbia-europos-centrinis-bankas')
    all_data = {}
    today = datetime.now() #kai reikia su datom
    for day in range(dienu_skaicius):
        day = today - timedelta(days=day)
        formated_date = day.strftime('%Y-%m-%d')
        url = f'{base_url}?class=Eu&type=day&selected_curr=&date_day={formated_date}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
        lb_table = []
        table = soup.find('table', class_='table')
        if table:
            headers = [header.get_text().strip() for header in table.find_all('th')]
            if not headers and table.find('tr'):
                headers = [f'stulpelis{i+1}' for i in range(len(table.find('tr').find_all('td')))]
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if columns:
                    row_data = {headers[i]: " ".join(column.get_text().strip().split()) for i, column in enumerate(columns)}
                    lb_table.append(row_data)
        all_data[formated_date] = lb_table
    return all_data
data_collected = banko_duomenu_gavimas('2024-03-01', 7)
df = pd.DataFrame()

for date, data in data_collected.items():
    df1 = pd.DataFrame(data)
    df1['Data'] = date
    df = pd.concat([df, df1], ignore_index=True)
df.to_csv('Valiutosbankas.csv', index=False)