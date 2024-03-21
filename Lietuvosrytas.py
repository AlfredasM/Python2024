
import requests
from bs4 import BeautifulSoup

def gauti_naujienas(url):
     response = requests.get(url)
     soup = BeautifulSoup(response.content, 'html.parser')

     naujienu_antraste = soup.find_all('h2', class_='LPostContent__title')
     return [antraste.text.strip() for antraste in naujienu_antraste]

#rezultatas = gauti_naujenas('https://www.lrytas.lt')
# print(rezultatas)

