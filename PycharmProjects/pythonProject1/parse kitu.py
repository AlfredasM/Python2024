# import requests
# from bs4 import BeautifulSoup
# def fetch_page(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
# def parse_page(url):
#     soup = BeautifulSoup(url, 'html.parser')
#     filmu_sarasas = []
#     filmai = soup.find_all('li', {'class': 'ipc-metadata-list-summary-item sc-1364e729-0 caNpAE cli-parent'})
#     for filmas in filmai:
#         filmo_pavadinimas = filmas.find('h3', class_='ipc-title__text').text.strip().replace('', '')[3:]
#         filmo_reitingas = float(filmas.find('span', class_='ipc-rating-star').text.strip().replace('\n', '')[:3])
#         metai = int(filmas.find('div', class_='sc-be6f1408-7 iUtHEN cli-title-metadata').find_all('span')[0].text)
#         trukme = filmas.find('div', class_='sc-be6f1408-7 iUtHEN cli-title-metadata').find_all('span')[1].text
#         kategorija = filmas.find('div', class_='sc-be6f1408-7 iUtHEN cli-title-metadata').find_all('span')[-1].text
#         filmu_sarasas.append({
#             'Filmo pavadinimas': filmo_pavadinimas,
#             'Reitingas': filmo_reitingas,
#             'Metai': metai,
#             'Trukme': trukme,
#             'Kategorija': kategorija
#         })
#     return filmu_sarasas
# def scrap_page(url):
#     visi_filmai = []
#     url = fetch_page(url)
#     if url:
#         has_objects = parse_page(url)
#         if has_objects:
#             visi_filmai.extend(has_objects)
#         else:
#             print('Nera daugiau filmu')
#     else:
#         print('Negauti duomenys')
#     print(f'Is viso filmu: {len(visi_filmai)}')
#     for filmas in visi_filmai:
#         print(filmas)
# url = 'https://www.imdb.com/chart/top/'
# scrap_page(url)

# https://www.fifaindex.com/

import requests
from bs4 import BeautifulSoup
import os

def parsisiusti_puslapi(url):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Puslapis pasiekimas: {url}")
        return response.text
    else:
        print(f"Nepavyko pasiekti puslapio. Svetainė grąžino {response.status_code}.")
        return None

def istraukti_zaideju_info(html):
    zaideju_info = []
    soup = BeautifulSoup(html, 'html.parser')
    zaidejai = soup.find_all('tr',  attrs={'data-playerid': True})
    for zaidejas in zaidejai:
        vardas = zaidejas.find('td', attrs={'data-title': "Name"}).text.strip()
        # print(vardas)

        age = int(zaidejas.find('td', attrs={'data-title': "Age"}).text.strip())

        team1 = zaidejas.find('td', attrs={'data-title': "Team"})
        team = team1.find('img').get('alt').strip().replace(' FIFA 24','')

        nationality1 = zaidejas.find('td', attrs={'data-title': "Nationality"})
        nationality = nationality1.find('img').get('alt').strip().replace(' FIFA 24', '')

        # OVR_POT = zaidejas.find_all('span', attrs={'class': 'badge badge-dark rating'}) # kažkodėl grąžina tuščią
        OVR_POT = zaidejas.find_all('span', class_='rating')
        # print(OVR_POT)
        OVR = int(OVR_POT[0].text.strip())
        POT = int(OVR_POT[1].text.strip())

        positions1 = zaidejas.find('td', attrs={'data-title': "Preferred Positions"})
        positions2 = positions1.find_all('span', class_='position')
        positions = [poz.text.strip() for poz in positions2]
        # positions = ', '.join(positions)

        zaidejo_info = {
            'Name': vardas,
            'Age': age,
            'Team': team,
            'Nationality': nationality,
            'OVR': OVR,
            'POT': POT,
            'Positions': positions
        }
        # print(zaidejo_info)
        zaideju_info.append(zaidejo_info)
    return zaideju_info


def nuskaityti_vietini_puslapi(html_rinkmena):
    turinys = ''
    with open(html_rinkmena, mode='r', encoding='utf-8') as rinkmena:
        turinys_eilutese = rinkmena.readlines()
        for eilute in turinys_eilutese:
            turinys += eilute
    return turinys

def irasyti_kaip_vietini(turinys, html_rinkmena):
    with open(html_rinkmena, mode='w', encoding='utf-8') as rinkmena:
        rinkmena.writelines(turinys)

def main():
    url = 'https://www.fifaindex.com/'
    html_rinkmena = 'FIFA_index.html'

    if os.path.exists(html_rinkmena):
        print("Bandoma įkelti iš vietinio HTML:", html_rinkmena)
        html = nuskaityti_vietini_puslapi(html_rinkmena)
    else:
        print("Bandoma pasiekti internetinį puslapį", url)
        html = parsisiusti_puslapi(url)
        # įrašyti pakartotiniam naudojimui, kad nebereiktų siųstis iš interneto
        irasyti_kaip_vietini(html, html_rinkmena)

    if html:
        print("Pavyko gauti HTML turinį.")
        zaideju_info = istraukti_zaideju_info(html)
        print("Gauti žaidėjai:", len(zaideju_info))
        # print(zaideju_info)
        for zaidejo_info in zaideju_info:
            print(zaidejo_info)
    else:
        print("Negalime pateikti filmų informacijos.")

main()

# https://spain-real.estate/property/andalusia/sevilla/

import requests
from bs4 import BeautifulSoup

def gauti_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Puslapis pasiekimas: {url}")
        return response.text
    else:
        print(f"Nepavyko pasiekti puslapio. Svetainė grąžino {response.status_code}.")
        return None

def isrinkti_info_apie_namus(html):
    namu_info = []
    soup = BeautifulSoup(html, 'html.parser')
    #namai = soup.find_all('div', {'class': 'info'})
    namai = soup.find_all('li', {'data-object': True})
    for namas in namai:
        pavadinimas = namas.find('div', class_='title').text.strip()

        kaina0 = namas.find('div', class_='price js-list-for-show')
        kaina1 = kaina0.find('span').text.strip()
        kaina = kaina1.replace('€ ','').replace('\xa0','')
        # kaina = int(kaina2)

        # params = namas.find('div', class_='params')
        # if params.text.strip() != ''

        miegamieji0 = namas.find('span', {'class': 'bedrooms'})
        if miegamieji0:
            miegamieji = int(miegamieji0.find('b').text.strip())
        else:
            miegamieji = None

        vonios0 = namas.find('span', {'class': 'bathrooms'})
        if vonios0:
            vonios = int(vonios0.find('b').text.strip())
        else:
            vonios = None

        plotas0 = namas.find('span', {'class': 'area'})
        if plotas0:
            plotas = plotas0.find('b').text.strip()
            plotas = float(plotas.replace(' m2', ''))
        else:
            plotas = None

        namo_info = {
            'Pavadinimas': pavadinimas,
            'Kaina': kaina,
            'Miegamieji': miegamieji,
            'Vonios': vonios,
            'Plotas': plotas
        }
        # print(namo_info)
        namu_info.append(namo_info)
    return namu_info

def scrap(base_url, nuo_puslapio=1, puslapiu_skaicius=10):
    # https://spain-real.estate/property/andalusia/sevilla/page/18/#objects
    visi_namai = []
    dabartinis_puslapis = nuo_puslapio
    while dabartinis_puslapis <= nuo_puslapio + puslapiu_skaicius - 1:
        url = f"{base_url}page/{dabartinis_puslapis}/"
        html = gauti_html(url)
        if html:
            namai = isrinkti_info_apie_namus(html)
            if namai:
                print(f"{dabartinis_puslapis} puslapyje rasta namų: {len(namai)}")
                visi_namai.extend(namai)
            else:
                print(f"{dabartinis_puslapis} puslapyje namų nerasta")
                break
        else:
            print(f"{dabartinis_puslapis} puslapyje namų net neieškome.")
            break
        dabartinis_puslapis += 1

    print("Iš viso rasta namų:", len(visi_namai))
    for namas in visi_namai:
        print(namas)

url = 'https://spain-real.estate/property/andalusia/sevilla/'
scrap(url, 1, 3)