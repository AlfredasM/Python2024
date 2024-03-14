import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt


class Info_traukykla:
    @staticmethod
    def fetch_page(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('Puslapis nepasiekiamas')
            return None

    def istraukti_visa_info(self, url):
        html = Info_traukykla.fetch_page(url)
        soup = BeautifulSoup(html, 'html.parser')
        orai = soup.find_all('div', {'class': "day-wrap"})
        # print('Informacija ištraukta') if orai else print('Informacija neištraukta')
        return orai


class Oru_info:

    @staticmethod
    def rodyti_info(orai):
        savaites_dienos = []
        savaites_datos = []
        savaites_temp = []

        for oras in orai:
            diena = oras.find('h4').text.strip()
            data = oras.find('div', class_="date").text.strip()
            temp = oras.find('div', class_="temprature").text.strip().replace('°C', '')
            savaites_dienos.append(diena)
            savaites_datos.append(data)
            savaites_temp.append(temp)

        data = {'Diena': savaites_dienos, 'Data': savaites_datos, 'Temperatura': savaites_temp}
        df = pd.DataFrame(data)
        return df


def analizuoti_temperaturas(df):
    df['Temperatura'] = pd.to_numeric(df['Temperatura'], errors='coerce')
    auksciausia_temp = df['Temperatura'].max()
    zemiausia_temp = df['Temperatura'].min()
    vidutine_temp = df['Temperatura'].mean()
    # print(f"Auksciausia temperatura: {auksciausia_temp}°C")
    # print(f"Zemiausia temperatura: {zemiausia_temp}°C")
    # print(f"Vidutine temperatura: {vidutine_temp:.2f}°C")
    max_temp_day = df.loc[df['Temperatura'].idxmax()]
    min_temp_day = df.loc[df['Temperatura'].idxmin()]
    # print(f'Auksciausia temperaturos diena: {max_temp_day["Diena"]} ({max_temp_day["Temperatura"]})')
    # print(f'Zemiausia temperaturos diena: {min_temp_day["Diena"]} ({min_temp_day["Temperatura"]})')
    plt.figure(figsize=(10, 6))
    plt.plot(df['Diena'], df['Temperatura'], marker='o', color='r', linestyle='-')
    plt.scatter(max_temp_day['Diena'], max_temp_day['Temperatura'], color='g', marker='o', zorder=5, label='Didziausia temperatura')
    plt.show()
    plt.scatter(min_temp_day['Diena'], min_temp_day['Temperatura'], color='y', marker='o', zorder=5, label='Zemiausia temperatura')





url = 'https://www.meteo.lt/'
informacija = Info_traukykla()
orai = informacija.istraukti_visa_info(url)
df_orai = Oru_info.rodyti_info(orai)

if df_orai is not None:
    analizuoti_temperaturas(df_orai)
else:
    print("Nera duomenu")