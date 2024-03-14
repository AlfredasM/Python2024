import requests
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.meteo.lt/'
response = requests.get(url)

#print(response)


soup = BeautifulSoup(response.content, 'html.parser')
week_days = soup.find_all('div', class_='week-day')

#print(week_days)

temperatura = soup.find_all('div', class_='temprature')

#print(temperatura)


filtered_week_days = [week_day.get_text(strip= True).split(' ')[0] for week_day in week_days]

#print(filtered_week_days)





