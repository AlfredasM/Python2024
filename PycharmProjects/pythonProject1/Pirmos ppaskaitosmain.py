#1 paskaita
# vardas = "Alfa" # string tipas
# amzius = 35 # int tipas
# kaina = 10.99 # float tipas
# ar_pilnametis =  True # boolean tipas
#
# print("tipo keitimas" , float (amzius))
#import json
import os.path
import random

# x = 5
# y = 10
#
# suma = x + y
# skirtumas = x - y
# sandauga = x * y
# dalmuo = x / y

#
# print("Suma:", suma)
# print("Skirtumas:", skirtumas)
# print("Sandauga:", sandauga)
# print("Dalmuo:", dalmuo)


# ar_lygu =  x == y
# ar_nelygu =x !=y
# daugiau = x > y
# maziau = x < y
# print (maziau)

# x = True
# y = False
# rezultatas = x and y
# rezultatas = x or y
# rezultatas = not x

# print(rezultatas)

x = 5
# x += 1
# #x -= 1
#
# # print(x)
#
# x = 10
# y = 15
#
# if x < y True else
#     print (x)

# pirkiniu_krepselis = ['Pienas', 'Duona', 'Obuolys','Sviestas']
#
# print(pirkiniu_krepselis [0])
# pilnametis = 18
# if pilnametis > 18:
#     print ("Jus esate pilnametis.")
# else:
#     print ("Jus esate nepilnametis.")

# mokinio_pazymiai = 10
#
# if mokinio_pazymiai < 4:
#         print('prastai')
#
# elif mokinio_pazymiai <= 6:
#     print('patenkinamai')
#
# elif mokinio_pazymiai >= 7:
#     print('gerai')
#
# elif mokinio_pazymiai = 10:
#     print ('puikiai')
# else:
#     print (error)
#
# skaicius = 20
# if skaicius /2:
#     print ('lyginis')
# else:
#     print ('nelyginis')
#
# zsakymo_suma = 30
# if uzsakymo_suma >=50:
#     print ('nemokamas uzsakymas')
# elife uzsakymo_suma <50:
#     print({uzsakymo_suma} +5=)
#
# uzsakymo_suma = 40
# suma = uzsakymo_suma if uzsakymo_suma >= 50 else uzsakymo_suma + 5
# print("Galutine suma su pristatymo mokesciu:", suma)
#
#
#
# skaicius = 1001
# liekana = skaicius % 2
# reiksme = "lyginis" if liekana == 0 else "nelyginis"
# print(reiksme)


#
# # vartotojai = {
# #     'Vardas':
# # }
#
# zodynas = [
#     {"vardas": "Jonas", "amzius": 30, "miestas": "Vilnius"}
# ]
#
# print (zodynas [1])
#
# studentas = {
#     'vardas': 'Ona'
#     'Pazymiai': { 'Matematika': 9}
#
# }
# zodynas = [
#     {"vardas": "Jonas", "amzius": 30, "miestas": "Vilnius"}

#
# # print (zodynas[0])
#
# # 2 paskaita
# # i raktas rezultatui gauti, paskutinis skaicius kas kelinta print
# for i in range (1, 11, 2):
#     print (i)
#     #atprintins nuo 0 iki 10
#
# skaiciai = [1, 2, 3, 4, 5]
#
# print(skaiciai)
#
# # zodynai
#
# darbuotojai = {
#     "vardas": 'Jonas',
#     "amzius": 30,
#     "Miestas": 'Vilnius'
# }
# # range - keys - items (print f"{key}:{value}")
# for darbuotojas in darbuotojai.items():
#     print(darbuotojas)

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(f"Ciklas sustojo nes kaicius {i} buvo pasiektas")

# for skaicius in range(1, 20):
#     if skaicius % 2 != 0:
#         continue
#     print(skaicius)

# vartotojai = {
#     'vardas': 'Jonas',
#     'amzius': '25',
#     'miestas': 'Vilnius'
# }
# raktas = input("Iveskite rakta kuri norite patikrinti zodyne:")
# raktas_egzistuoja = False
#
# for key in vartotojai:
#     if key == raktas:
#         raktas_egzistuoja = True
#         break
#
# print (raktas_egzistuoja)

# sakiniai = [
#     'Labas rytas studentai',
#     'Python yra nuostabi programavimo kalba',
#     'Dabar mokomes dirbti su ciklais'
# ]
#
# bendras_zodziu_skaicius = 0
#
#
# for sakinys in sakiniai:
#     bendras_zodziu_skaicius +=len(sakinys.split())
# print (f"Bendras zodziu skaicius sakiniuose yra:{bendras_zodziu_skaicius}")
# CIKLAI WHILE

# skaicius = 1
# while skaicius <= 5:
#     print (skaicius)
#     skaicius +=1

# while True:
#     x = int(input("Iveskite skaiciu>"))
#     if x < 0:
#         break
# print ("Ivestas teigiamas skaicius", x)

# suma = 0
# while True:
#     skaicius = int(input("Iveskite skaiciu (0 - uzdaryti programa)_>"))
#     if skaicius == 0:
#         break
#         suma += skaicius
# print (f"Skaiciu suma: {suma}")



# suma = 0
# while True:
#     skaicius = int(input("Iveskite skaiciu (0 - uzdaryti programa)_>"))
#     if skaicius == 0:
#         break
#     suma += skaicius
# print(f"Skaiciu suma: {suma}")
#
# miestas = "Kaunas"
# gyventoju_skaicius = 50000
# yra_Uostamiestis = True
#
#
#
#
#
# print ('Miestas:' , miestas , '\nGyventoju skaicius:' , gyventoju_skaicius )

# sarasas  = range (1,5)
# for sk in sarasas:
#     print(sk)
#     if sk <5:
#         print('AAA')

# simtas = range(1, 101)
# suma = 0
# for skaicius in simtas:
#     suma = suma + skaicius
# print(suma)

# sakinys = "Labas rytas, pasauli"
# sarasas =[1, 5, 8, 9, 11]
# zodziai = sakinys.split()
# skaicius = len(sarasas)
# print(skaicius)
# # bendras_zodziu_skaicius = 0
# #
# # for zodziai in sakinys:
# #     bendras_zodziu_skaicius += len(zodziai.split())
# #
# # print(f"Bendras zodziu skaicius sakinyje yra:{bendras_zodziu_skaicius}")

# zodis = "Labas"
# atvirksciai = ""
# for raide in zodis:
#     atvirksciai = raide + atvirksciai
# print (atvirksciai)

# darbuotojai = [
#     {'Vardas': "Jonas",
#      "Atlyginimas": 500},
#
#     {'Vardas': "Ona",
#      "Atlyginimas": 2000},
#
#     {'Vardas': "Juozas",
#      'Atlyginimas': 2000}
# ]
# bendras_atlyginimas = 0
# for darbuotojas in darbuotojai:
#     bendras_atlyginimas = bendras_atlyginimas + darbuotojas['Atlyginimas']
#     print(f"darbuotojas  {darbuotojas['Vardas']}, atlyginimas:{darbuotojas['Atlyginimas']}")
#
#
#
# vidutinis_atlyginimas = bendras_atlyginimas / len(darbuotojai)
#
# print(f"vidutinis atlyginimas = {vidutinis_atlyginimas}")
# kategorijos = {
#     'obuolys': 'vaisiai',
#     'slyva': 'vaisiai',
#     'bulve': 'darzoves',
#     'agurkas': 'darzoves'
#
# }
# prekes = [
#     'obuolys', 'bulve', 'slyva'
# ]
#
# grupuoti_pagal_kategorija = {
#
# }
#
# for preke in prekes:
#     kategorija = kategorijos[preke]
#     if kategorija in grupuoti_pagal_kategorija:
#         grupuoti_pagal_kategorija[kategorija].append(preke)
#     else:
#         grupuoti_pagal_kategorija[kategorija] = [preke]
# print(grupuoti_pagal_kategorija)

# ivestis = -1
# while ivestis <0:
#     ivestis = float(input("Iveskite teigiama skaiciu_>"))
# print (ivestis)

# Sukurkite programą, kuri naudodama while ciklą, suskaičiuoja
# ir atspausdina bet kurio įvesto skaičiaus skaitmenų sumą
# (pvz., skaičiaus 12345 skaitmenų suma yra 15).

# ivestis = input("Įveskite skaičių: ")
# skaicius = int(ivestis)  # Konvertuojame įvestį į sveikąjį skaičių

# skaicius = 12345

# Inicijuojame skaitmenų sumos kintamąjį
# suma = 0
#
# while skaicius > 0:
#     suma = suma + skaicius % 10  # Pridedame paskutinį skaitmenį prie sumos
#     skaicius = skaicius // 10  # Pašaliname paskutinį skaitmenį iš skaičiaus
#
# print(f"Įvesto skaičiaus skaitmenų suma yra: {suma}")

# Parašykite programą, kuri naudoja while ciklą ir if sąlygas, kad pašalintų visus duplikatus iš sąrašo.
# Pavyzdžiui, jei pradinis sąrašas yra skaiciai = [1, 2, 2, 3, 4, 4, 5],
# galutinis sąrašas turėtų būti [1, 2, 3, 4, 5].


# skaicius = 1
# while True:
#     skaicius = int(input("Iveskite skaiciu (0 - uzdaryti programa)_>"))
#     if skaicius == 0:
#         break
#
# print()
# skaicius = 1
# skaicius = int(input("Iveskite skaiciu _>"))
#
#
# print(skaicius)


#
# try:
#     ivestis = int(input('Prasome ivesti skaiciu_>'))
#     print(ivestis)
# except ValueError:
#     print("Neteisinga ivestis prasome ivesti skaiciu!")
# except TypeError:
#     print("Neteisinga")

# try:
#     numbers = [1, 2, 3]
#     print (numbers[0])
# except IndexError as e:
#     print("Indekso klaida:", e)

# ivestis = int(input('Prasome ivesti skaiciu_>'))
# print(ivestis)
# except ValueError:\
#     print("Neteisinga ivestis prasome ivesti skaiciu!")
# except TypeError:\
#     print("Neteisinga")

# try:
#     indeksas = [1, 2, 3, 4, 5]
#     print("Skaicius:", indeksas[0])
# except IndexError as e:
#     print("Indekso klaida:", e)
#
# ivestis = input ("Iveskite savo amziu")
# ivestis = int (ivestis)

# try:
#     print("Jusu amzius:", ivestis)
# except IndexError as e:
#     print("Ivestas ne skaicius", e)
#
# ivestis = input("Iveskite savo amziu")
# ivestis = int(ivestis)
# ivestis = input("Iveskite savo amziu")
# ivestis = int(ivestis)
#
# try:
#     print("Jusu amzius:", ivestis)
#
# except IndexError as e:
#     print("Neteisingai ivestas amzius: iveskite amziu is naujo", e)
#
# while True:
#
#     try:
#         ivestis = int(input('Prasome ivesti savo amziu metais_>'))
#         print(f" Jusu amzius yra:{ivestis}")
#         break
#
#     except ValueError as e:
#         print('Neteisingai ivestas skaicius!', e)

# ivestis = int(input('Prasome ivesti skaiciu_>'))
import requests
from bs4 import BeautifulSoup

# url = "https://delfi.lt"
# 200 OK
# 403 Forbidden
# 500 Server error
# antrastes = []
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         # print(f"Puslapis pasiekiamas: \n{response.content}")
#         # soup turinio apsibrezimas
#         soup = BeautifulSoup (response.content,  'html.parser')
#         title = soup.find('title').text
#         #print(f"Puslapio pavadinimas" {title})
#         antrasciu_tekstas = soup.find_all('h5')
# except requests.ConnectionError:
#     print("Puslapis Nepasiekiamas")

#url = "https://delfi.lt"
# 200 OK
# 403 Forbidden
# 500 Server error
#antrastes = []

# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         # print(f"Puslapis pasiekiamas: \n{response.content}")
#         soup = BeautifulSoup(response.content,'html.parser')
#         puslapio_pavadinimas = soup.find('title').text
#         # print(f"Puslapio pavadinimas: {puslapio_pavadinimas}")
#         anstrasciu_tekstas = soup.find_all('article', attrs={'class': 'C-block-type-102-headline'})
#         for anstraste in anstrasciu_tekstas:
#             antrastes_pavadinimas = anstraste.find('h5', attrs={'class': 'C-headline-title'}).text.strip()
#             antrastes.append({
#                 'Antraste': antrastes_pavadinimas
#             })
#     print(antrastes)
#
# except requests.ConnectionError:
#     print("Puslapis Nepasiekiamas")

# import requests
# from bs4 import BeautifulSoup
# url = "https://15min.lt"
# antraste = []
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         #print("Puslapis pasiekiamas: \n{response.content}")
#         soup = BeautifulSoup(response.content, 'html.parser')
#         antrasciu_tekstas = soup.find_all('article', class_='item-article')
#         #print(antrasciu_tekstas)
#         for antraste in antrasciu_tekstas:
#             antrasciu_pavadinimas = antraste.find('h4', class_='vl-title item-no-front-style').text.strip()
#             antrastes.append({
#                 'Antrastes': antrasciu_pavadinimas
#             })
#         print(antrastes)
#
# except requests.ConnectionError:
#     print("Puslapis Nepasiekiamas")
#         # soup = BeautifulSoup(response.content, 'html.parser')
#         # puslap

# ulr = "https://www.rde.lt/categories/lt/150/sort/5/filter/0_0_0_0/page/1/Ne%C5%A1iojami-kompiuteriai.html"
# produktai = []
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         #print("Puslapis pasiekiamas: \n{response.content}")
#     soup = BeautifulSoup(response.content, 'html.parser')
#     produktas = soup.find_all('li', class_='col col--xs-4 product js-product js-touch-hover')
#    print(produktas)
#     for prod in produktas:
#         produkto_pavadinimas = prod.find('h3', class_='product_title').text.strip()
#         print(produkto_pavadinimas)
# except requests.ConnectionError:
#    # print("Puslapis Nepasiekiamas")

#RASOS PVZ

# url = "https://rde.lt/categories/lt/150/sort/5/filter/0_0_0_0/page/1/Nešiojami-kompiuteriai.html"
# produktai = []
#
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         # print(f"puslapis pasiekiamas: ")
#         soup = BeautifulSoup(response.content, 'html.parser')
#         produktas = soup.find_all('li', class_='col col--xs-4 product js-product js-touch-hover')
#         # print(produktas)
#         for prod in produktas:
#             produkto_pavadinimas = prod.find('h3', class_='product__title').text.strip()
#             print(produkto_pavadinimas)
#
# except requests.ConnectionError:
#     print("Puslapis nepasiekiamas")

#Namu darbas Kilobaitas

# url = "https://www.kilobaitas.lt/paieskos_rezultatai/searchresult.aspx?q=ssd&limit=40&c=651"
# produktai = []
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         #print(f"Puslapis pasiekiamas: \n{response.content[:1000]}")
#         soup = BeautifulSoup(response.content, 'html.parser')
#         puslapio_pavadinimas = soup.find('title').text
#         #print(f"Puslapio pavadinimas: {puslapio_pavadinimas}")
#         produktai_visi = soup.find_all('div', class_='item col-lg-3 col-md-4 col-sm-6 respl-item')
#         #print(produktai)
#         for pro_pav in produktai_visi:
#             produktu_pavadinimas = pro_pav.find('div', class_="item-title line-clamp").text.strip()
#             produktai.append({
#            'Produktai': produktu_pavadinimas})
#     print(produktai)
#
#
# except requests.ConnectionError:
#     print("Puslapis nepasiekiamas")

#4 paskaita

# def pasisveikinimas(vardas='Svecias'):
#     return f"Labas, {vardas}"
# funkcijos_kvietimas = pasisveikinimas()
# print(funkcijos_kvietimas)

# def suma(x, y):
#     print(f"Suma: {x+y}")
# suma(5, 9)
#

#
# skaicius1 = 5
# skaicius2 = 10
#
#
# def keisti_globalu():
#     global skaicius1
#     skaicius1 = 20
#
#
# keisti_globalu()
# print(skaicius1)

# def vidurkis(skaiciai):
#     if not skaiciai:
#         return 0
#     return sum(skaiciai) / len (skaiciai)
# skaiciu_sarasas = [10, 20, 30, 40]
# vidurkis = vidurkis (skaiciu_sarasas)
# print (vidurkis)

# def raidziu_pasikartojimas(zodis):
#     raidziu_skaicius = {}
#     for raide in zodis:
#         if raide in raidziu_skaicius:
#             raidziu_skaicius[raide] +=1
#         else:
#             raidziu_skaicius[raide] = 1
#     return
#     zodis = "Pasikalbekime"
#     manoFunkcija = raidziu_pasikartojimas(zodis)
#     print(manoFunkcija)

# def zodziu_ilgiai(sarasas):
#     ilgiu_sarasas = []
#     for zodis in sarasas:
#         ilgiu_sarasas.append(len(zodis))
#     return ilgiu_sarasas
# zodziu_sarasas = ['Man', "Labai", 'patinka', 'Phyton']
# ilgiu_sarasas = zodziu_ilgiai (zodziu_sarasas)
# print(ilgiu_sarasas)

# def rast_min_max(skaiciai):
#     min_skaiciai = skaiciai[0]
#     max_skaiciai = skaiciai[0]
#     for sk in skaiciai:
#         if sk < min_skaiciai:
#             min_skaiciai = sk
#         elif sk > max_skaiciai:
#             max_skaiciai = sk
#     return min_skaiciai, max_skaiciai
#
#
# skaiciai = [10, 2, 22, 3, 56]
# print(rast_min_max(skaiciai))

#n = 0
# def seka_x_n(x, n):
#
#     print({x + (n + 1)})
#     n += 1
#     seka_x_n(2, 3)

# def skaiciu_sarasas(sarasas):
#     skaiciai= []
#     for sk in skaiciai:
#         if sk > skaiciai:
#             return skaiciai
# skaiciai = [1, 2, 3, 5, 10]
#
# print(skaiciai)

# def ar_pirminis(skaicius):
#     if skaicius <= 1:
#         return False
#     for i in range(2, int(skaicius ** 0.5) + 1):
#         if skaicius % i == 0:
#             return False
#         return True
# print(ar_pirminis(11))

#Rasos var

# def pirminis_skaicius(skaicius):
#     if skaicius <= 1:
#         return False
#     for i in range(2, int(skaicius**0.5)+1):
#         if skaicius % i == 0:
#          return False
#     return True
# print(pirminis_skaicius(2))


# def zodis()
#     apverstas = ""
#
#
# for raide in zodis:
#     apv_zodis = raide + apverstas
# return
#
# zodis = "Tekstas"
#
# funkcija = apv_zodis
# print(funkcija)

#5 paskaita failu skaitymas rasymas json. failai

# tekstas = "As gyvenu gerai"
# tekstas2 = "\nman yra 35 metai"
# with open('duomenys.txt', 'w+', encoding='utf-8') as file:
#     file.write(tekstas+tekstas2)
#     file.seek(0)
#     turinys = file.read()
#     print(turinys)

# import json
#
# duomenys = {
#     'vardas': 'Antanas',
#     'amzius': 32,
#     'miestas': 'Kaunas'
# }
#
# with open('data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# # print(data)
#
# data['vartotojai'].append(duomenys)
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)


# import json
#
#
# def atnaujinti_json_faila(failo_pavadinimas, atnaujinimo_rezimas):
#     try:
#         with open(failo_pavadinimas, 'r', encoding='utf-8') as file:
#             duomenys = json.load(file)
#     except FileNotFoundError:
#         duomenys = {}
#
#     duomenys = atnaujinimo_rezimas(duomenys)
#
#     with open(failo_pavadinimas, 'w', encoding='utf-8') as file:
#         json.dump(duomenys, file, ensure_ascii=False, indent=4)
#
#
# def prideti_nauja_knyga(duomenys):
#     if 'knygos' not in duomenys:
#         duomenys['knygos'] = []
#     duomenys['knygos'].append({
#         'id': 2,
#         "pavadinimas": "Ismok programuoti su python",
#         'autorius': "Antanas Antanavicius"
#     })
#     return duomenys
#
#
# atnaujinti_json_faila('duomenys.json', prideti_nauja_knyga)

# zodis1 = "anglis"
# zodis2 = "\n2bebras"
# zodis3 = "\nantarktida"
# with open('zodziai.txt', 'w', encoding='utf-8') as file:
#     file.write(zodis1)
#     file.write(zodis2)
#     file.write(zodis3)

# with open('studentai.json', 'r', encoding='utf-8') as file:
#     studentai = json.load(file)
#
# print(studentai)

#uzdavinys su automobiliu

# class Automobilis:
#     def __init__(self, marke, spalva, modelis):
#         self.marke = marke
#         self.spalva = spalva
#         self.modelis = modelis
#
#     def info(self):
#         print(f" Marke: {self.marke}, Spalva: {self.spalva}, Modelis: {self.modelis}")
#
#
# toyota = Automobilis("Toyota", 'Violetine', 'Avensis')
# mazda = Automobilis("Mazda", 'Raudona', 'CX6')
# toyota.info()
# mazda.info()

# uzdavinys darbuotojai
# class Darbuotojai:
#     def __init__(self):
#         self.darbuotoju_sarasas = []
#
#     def prideti_darbuotoja(self,vardas, pareigos, atlyginimas):
#         self.darbuotoju_sarasas.append({
#             'vardas': vardas,
#             'pareigos': pareigos,
#             'atlyginimas': atlyginimas
#         })
#         print(f"Darbuotojas: {vardas} pridetas!")
#
#     def info(self):
#         print(f"Darbuotojas: {self.darbuotoju_sarasas}")
#
# imone = Darbuotojai()
# imone.prideti_darbuotoja("Jonas Jonaitis","Programuotojas", 2000)
# imone.info()

#uzdavinys destytojo
# class Darbuotojai:
#     def __init__(self):
#         self.darbuotoju_sarasas = []
#
#     def prideti_darbuotoja(self, vardas, pareigos, atlyginimas):
#         self.darbuotoju_sarasas.append({
#             'vardas': vardas,
#             'pareigos': pareigos,
#             'atlyginimas': atlyginimas
#         })
#         print(f"Darbuotojas: {vardas} pridetas!")
#
#     def salinti_darbuotoja(self, vardas):
#         for darbuotojas in self.darbuotoju_sarasas:
#             if darbuotojas['vardas'] == vardas:
#                 self.darbuotoju_sarasas.remove(darbuotojas)
#                 print(f"Darbuotojas: {vardas} buvo pasalintas!")
#                 return
#         print(f"Darbuotojas: {vardas} nerastas!")
#
#     def ieskoti_darbuotojo_pagal_varda(self, vardas):
#         rasti_darbuotojai = [darbuotojas for darbuotojas in self.darbuotoju_sarasas if vardas.lower() in darbuotojas["vardas"].lower()]
#         if rasti_darbuotojai:
#             return rasti_darbuotojai
#         else:
#             return "Darbuotoju su tokiu vardu nerasta!"
#
#     def info(self):
#         print(f"Darbuotojas: {self.darbuotoju_sarasas}")
#
#
# imone = Darbuotojai()
# imone1 = Darbuotojai()
# imone.prideti_darbuotoja("Jonas Jonaitis", "Programuotojas", 2000)
# imone1.prideti_darbuotoja("Antanas", "Vadybininkas", 1500)
# imone1.prideti_darbuotoja("Petras", "Direktorius", 3500)
# # imone1.salinti_darbuotoja('Petras')
# print(imone1.ieskoti_darbuotojo_pagal_varda("Jonas"))
# imone.info()
# imone1.info()

#6 paskaita
# aatsakingaas uz filtravima
#import os

#atsakingas uz move rename perkelti ir t.t
# import shutil
# import os
#
#
# class FileOrganizer:
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#
#     def organizer(self):
#         # patikriname ar aplankas egzistuoja
#         if not os.path.exists(self.folder_path):
#             print (f"The folder {self.folder_path} doesn't exist")
#         # Perziureti visus failus nurodytame aplanke
#
#         for item in os.listdir(self.folder_path):
#             item_path = os.path.join(self.folder_path, item)
#             #jei tai failas
#             if os.path.isfile(item_path):
#                 #isskirti pagal pletini
#                 file_extension = item.split('.')[-1].lower() #.jpg, .pdf
#                 if file_extension == item: #jei failas neturi pletinio
#                     continue
#                     #perkeliame faila i atitinkma aplanka
#                 self._move_file(item_path, file_extension)
#             print("File organization completed!")
#
#     def _move_file(self, item_path, file_extension):
#         # sukursime nauja aplanka pletiniui jei jis dar neegzistuoja
#         extension_folder_path = os.path.join(self.folder_path, file_extension)
#         if not os.path.exists(extension_folder_path):
#             os.makedirs(extension_folder_path)
#             # Perkeliame faila i nauja aplanka
#         shutil.move(item_path, extension_folder_path)
#         print(f"Moved {os.path.basename(item_path)} -> {extension_folder_path}/")
#
#
# # Tik Windows
#
# desktop_path = os.path.join(os.path.join(os.environ ['USERPROFILE']), 'Documents')
# file_organizer = FileOrganizer(desktop_path)
# file_organizer.organizer()


#papildomi veiksmai
# import shutil
# import os
#
#
# class FileOrganizer:
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         self.actions = []
#
#     def organize(self):
#         # patikriname ar aplankas egzistuoja
#         if not os.path.exists(self.folder_path):
#             print (f"The folder {self.folder_path} doesn't exist")
#         # Perziureti visus failus nurodytame aplanke
#
#         for item in os.listdir(self.folder_path):
#             item_path = os.path.join(self.folder_path, item)
#             #jei tai failas
#             if os.path.isfile(item_path):
#                 #isskirti pagal pletini
#                 file_extension = item.split('.')[-1].lower() #.jpg, .pdf
#                 if file_extension == item: #jei failas neturi pletinio
#                     continue
#                     #perkeliame faila i atitinkma aplanka
#                 self._move_file(item_path, file_extension)
#             print("File organization completed!")
#
#     def _move_file(self, item_path, file_extension):
#         # sukursime nauja aplanka pletiniui jei jis dar neegzistuoja
#         extension_folder_path = os.path.join(self.folder_path, file_extension)
#         if not os.path.exists(extension_folder_path):
#             os.makedirs(extension_folder_path)
#         final_path = os.path.join(extension_folder_path, os.path.basename(item_path))
#
#             # Perkeliame faila i nauja aplanka
#         shutil.move(item_path, extension_folder_path)
#         print(f"Moved {os.path.basename(item_path)} -> {extension_folder_path}/")
#         self.actions.append((final_path, item_path)) #nauja vieta, sena vieta
#
#     def undo_last_action(self):
#         if not self.actions:
#             print("No actions")
#             return
#         #gaauti paskutini veiksma ir ji atsaukti
#         last_action = self.actions.pop()
#         shutil.move(last_action[0], last_action[1])
#         print(f"Canceled: {os.path.basename(last_action[1])} <- {os.path.dirname(last_action[0])}/")
#     def interactive_mode(self):
#         while True:
#             print("File Organizer")
#             print("\n1. Move files\n2. Undo last action\n3.Quit")
#             choice = input ("Select options:")
#             if choice == "1":
#                 self.organize()
#             elif choice == "2":
#                 self.undo_last_action()
#             elif choice == "3":
#                 print("Exiting..")
#                 break
#             else:
#                 print("Invlid option please try again!")
#
#
# # Tik Windows
#
# desktop_path = os.path.join(os.path.join(os.environ ['USERPROFILE']), 'Documents')
# file_organizer = FileOrganizer(desktop_path)
# file_organizer.interactive_mode()


#Objektinis

# class Studentas:
#     def __init__(self, vardas, pavarde, studiju_programa):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.studiju_programa =studiju_programa
#
# #pakeisti objektus i tekstus funkcija
#     def __str__(self):
#         return f'{self.vardas} {self.pavarde} {self.studiju_programa}'
#
#
# class StudentuValdymoSistema:
#     def __init__(self):
#         self.studentai = []
#     def prideti_studenta(self, studentas):
#         self.studentai.append(studentas)
#         print(f"Studentas {studentas} pridetas sekmingai!")
#
#     def salinti_studenta(self, vardas, pavarde):
#         for studentas in self.studentai:
#             if studentas.vardas == vardas and studentas.pavarde == pavarde:
#                 self.studentai.remove(studentas)
#                 print(f"Studentas {vardas} {pavarde} pasalintas sekmingai")
#                 return
#         print("Studentas nerastas")
#
#     def atnaujinti_studento_info(self, vardas, pavarde, nauja_programa):
#         for studentas in self.studentai:
#             if studentas.vardas == vardas and studentas.pavarde == pavarde:
#                 studentas.studiju_programa = nauja_programa
#                 print(f"Studento {vardas} {pavarde} informacija atnaujinta sekmingai!")
#                 return
#             print("Studentas nerastas")
#     def rodyti_studentus(self):
#         if not self.studentai:
#             print("Studentu sarasas tuscias")
#             return
#         for studentas in self.studentai:
#             print(studentas)
#
# sistema = StudentuValdymoSistema()
#
# studentas1 = Studentas("Jonas", "Jonaitis", "Informatika")
# studentas2 = Studentas("Antanas", "Antanaitis", "Genetika")
#
# sistema.prideti_studenta(studentas1)
# sistema.prideti_studenta(studentas2)
#
# print("\n Visi studentai:")
# sistema.rodyti_studentus()
#
# print('--------------')
#
# sistema.atnaujinti_studento_info("Jonas","Jonaitis", "Programu sistemu inzinerija")
#
# print("\n Visi studentai po atnaujinimo:")
# sistema.rodyti_studentus()
#
# sistema.salinti_studenta("Jonas","Jonaitis")
# print('-------------')
# print("\nGalutinis studentu sarasas")
#
# sistema.rodyti_studentus()


#Sukurkite paprastą receptų valdymo sistemą naudojant Python.
# Ši sistema leis vartotojui įvesti receptus, juos saugoti, ieškoti pagal pavadinimą ir peržiūrėti visus įrašytus receptus.

# class Receptas:
#     def __init__(self, pavadinimas, produktas1, produktas2, produktas3):
#         self.pavadinimas = pavadinimas
#         self.produktas1 = produktas1
#         self.produktas2 = produktas2
#         self.produktas3 = produktas3
#     def __str__(self):
#         return f'{self.pavadinimas} {self.produktas1} {self.produktas2} {self.produktas3}'
#
# class ReceptuValdymosistema:
#     def __init__(self):
#         self.Receptai = []
#
#     def prideti_recepta (self, Receptas):
#         self.Receptai.append(Receptas)
#     print(f"Receptas {Receptas} pridetas sekmingai!")
#
#     def salinti_recepta (self, Receptas):
#         for receptas in self.Receptai:
#             if receptas.pavadinimas == pavadinimas:
#                 self.Receptai.remove(Receptas)
#                 print(f"Receptas {pavadinimas} pasalintas sekmingai")
#                 return
#             print("Receptas nerastas")
#
#     def ieskoti_recepto (self, Receptas):
#         for receptas in self.Receptai:
#             if receptas.pavadinimas == pavadinimas:
#                 print(f"Receptas {pavadinimas} rastas")
#                 return
#             print("Receptas nerastas")
#     def rodyti_receptus (self):
#         if not self.Receptai:
#             print("Receptu sarasas tuscias")
#             return
#         for Receptas in self.Receptai:
#             print(Receptas)
#
#
# sistema = ReceptuValdymosistema()
#
# receptas1 = Receptas("Kiausiniene", "kiausiniai", "vanduo","sviestas")
# receptas2 = Receptas("Pyragas","Cukrus","Pienas", "vanile")
# receptas3 = Receptas("Sriuba","vanduo", "bulves", "morkos")
#
# sistema.prideti_recepta(receptas1)
# sistema.prideti_recepta(receptas2)
# sistema.prideti_recepta(receptas3)
#
# print("\n Visi receptai")
# sistema.rodyti_receptus()
#
#
#
# sistema.salinti_recepta(Sriuba)
#
#
# sistema.ieskoti_recepto(Pyragas)
#
# sistema.rodyti_receptus()
#
#destytojo pavizdys
# class Receptas:
#     def __init__(self, pavadinimas, ingredientai, instrukcijos):
#         self.pavadinimas = pavadinimas
#         self.ingredientai = ingredientai
#         self.instrukcijos = instrukcijos
#
#     def __str__(self):
#         return f"{self.pavadinimas}\nIngredientai: {', '.join(self.ingredientai)}\nInstrukcijos: {self.instrukcijos}"
#
#
# class ReceptuValdymoSistema:
#     def __init__(self):
#         self.receptai = []
#
#     def prideti_recepta(self, receptas):
#         self.receptai.append(receptas)
#         print(f"Receptas '{receptas.pavadinimas}' pridėtas sėkmingai.")
#
#     def rasti_recepta(self, pavadinimas):
#         for receptas in self.receptai:
#             if receptas.pavadinimas.lower() == pavadinimas.lower():
#                 print(receptas)
#                 return
#         print("Receptas nerastas.")
#
#     def rodyti_receptus(self):
#         if not self.receptai:
#             print("Receptų sąrašas tuščias.")
#             return
#         for receptas in self.receptai:
#             print(receptas)
#             print("-" * 40)  # Skirtukas tarp receptų
#
#
# def main():
#     sistema = ReceptuValdymoSistema()
#
#     while True:
#         print("\nReceptų Valdymo Sistema")
#         print("1. Pridėti receptą")
#         print("2. Ieškoti recepto pagal pavadinimą")
#         print("3. Rodyti visus receptus")
#         print("4. Išeiti")
#         pasirinkimas = input("Pasirinkite veiksmą: ")
#
#         if pasirinkimas == '1':
#             pavadinimas = input("Įveskite recepto pavadinimą: ")
#             ingredientai = input("Įveskite ingredientus atskirtus kableliu: ").split(',')
#             instrukcijos = input("Įveskite gamybos instrukcijas: ")
#             receptas = Receptas(pavadinimas, ingredientai, instrukcijos)
#             sistema.prideti_recepta(receptas)
#         elif pasirinkimas == '2':
#             pavadinimas = input("Įveskite recepto pavadinimą, kurį norite rasti: ")
#             sistema.rasti_recepta(pavadinimas)
#         elif pasirinkimas == '3':
#             sistema.rodyti_receptus()
#         elif pasirinkimas == '4':
#             break
#         else:
#             print("Neteisingas pasirinkimas. Bandykite dar kartą.")
#
#
# if __name__ == "__main__":
#     main()











#Message pythonbasics


# 6 paskaita

#vatotoju sarasa , kur kiekvienas zmogus aprasytas

# vartotojai = [
#     {"Vardas": "Tomas", "Amzius": 30},
#     {"Vardas": "Kestas", "Amzius": 25},
#     {"Vardas": "Maryte", "Amzius": 22},
#     {"Vardas": "Lina", "Amzius": 28}
# ]
# valid_input = False
# while not valid_input:
#     try:
#         min_amzius = int(input("iveskite minimalu amziu_>"))
#         valid_input = True
#     except ValueError:
#         print("Klaida: prasome ivesti skaiciu")
#
# print("Vartotojai atitinkantys amziaus kriteriju:")
# for vartotojas in vartotojai:
#     if vartotojas["Amzius"] >= min_amzius:
#         print(vartotojas["Vardas"])

# Sukurkite programą, kuri leidžia vartotojui įvesti studentų vardus ir jų pažymius. Studentai ir jų pažymiai turėtų būti saugomi žodyne,
# kur vardai yra raktai, o pažymiai - sąrašo reikšmės. Vartotojas turėtų turėti galimybę įvesti kelis pažymius kiekvienam studentui.
# Programa turėtų apskaičiuoti ir atspausdinti kiekvieno studento pažymių vidurkį.
# Jei įvedant pažymius įvyksta klaida (pvz., įvedamas tekstas vietoj skaičiaus), programa turėtų informuoti vartotoją ir leisti įvesti pažymį iš naujo.




#Parašykite programą, kuri leidžia vartotojui valdyti prekių sąrašą. Vartotojas turėtų turėti galimybę pridėti naują prekę,
# pašalinti prekę ir peržiūrėti esamą prekių sąrašą.
# Prekės turėtų būti saugomos sąraše. Jei vartotojas bando pašalinti prekę, kuri neegzistuoja sąraše, programa turėtų informuoti apie klaidą.)

# CRUD - create , read, update, delete
# prekes = []
#
# while True:
#     ivestis = input("Pasirinkite veksma: prideti, perziureti, istrinti, iseiti_>")
#     if ivestis == 'iseiti':
#         break
#     elif ivestis == 'prideti':
#         preke = input("Iveskite prekes ppaavdinima")
#         prekes.append(preke)
#     elif ivestis == "istrinti":
#         preke = input("Iveskite pasalinamos prekes pavadinima_>")
#         try:
#             preke.remove(preke)
#         except ValueError:
#             print("Tokios prekes sarase nera!")
#     elif ivestis == 'perziureti':
#         print("Prekiu sarasas")
#         for preke in prekes:
#               print(preke)
#         else:
#             print("Neteisingas veiksmaas!")

# Parašykite programą, kuri paprašytų vartotojo įvesti metus ir mėnesio numerį (1 iki 12),
# o tada atspausdintų, kiek dienų yra tame mėnesyje.
# Atkreipkite dėmesį į keliamuosius metus.
# Jei įvestis neteisinga, programa turėtų informuoti vartotoją apie klaidą naudodama try ir except.

# def ar_keliamieji(metai):
#     if metai % 4 == 0:
#         if metai % 100 == 0:
#             if metai % 400 ==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#  #metai % 4 ==0 and (metai %100 !=0 or metai % 400 ==0)
#
# menesiu_dienos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# try:
#     metai = int(input("Iveskite metus_>"))
#     menesis =int(input("Iveskite menesio numeri (1-12)_>"))
#     if menesis <1 or menesis >12:
#         print("Klaida: menesio numeris turi buti tarp 1 ir 12")
#     else:
#         dienos = menesiu_dienos[menesis -1]
#         if menesis == 2 and ar_keliamieji(metai):
#             dienos += 1
#         print(f"{menesis} menesis {metai} metais turi {dienos} dienas")
# except ValueError:
#     print("Ivyko klaida: prasome ivesti skaicius!")

# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)
#
#
# def check_winner(board, player):
#     win_conditions = [
#         [board[0][0], board[0][1], board[0][2]],
#         [board[1][0], board[1][1], board[1][2]],
#         [board[2][0], board[2][1], board[2][2]],
#         [board[0][0], board[1][0], board[2][0]],
#         [board[0][1], board[1][1], board[2][1]],
#         [board[0][2], board[1][2], board[2][2]],
#         [board[0][0], board[1][1], board[2][2]],
#         [board[2][0], board[1][1], board[0][2]]
#     ]
#     return [player, player, player] in win_conditions
#
#
# def get_free_positions(board):
#     free_positions = []
#     for r in range(3):
#         for c in range(3):
#             if board[r][c] == " ":
#                 free_positions.append((r, c))
#     return free_positions
#
#
# def player_move(board, player):
#     while True:
#         try:
#             row = int(input(f"Zaidejas {player}, iveskite eilutes numeri(1-3)_>")) - 1
#             col = int(input(f"Zaidejas {player}, iveskite stulpelio numeri(1-3)_>")) - 1
#             if board[row][col] == " ":
#                 board[row][col] = player
#                 break
#             else:
#                 print("Pozicijos vieta uzimta! Prasome pasirinkti kita pozicijos vieta!")
#         except (ValueError, IndexError):
#             print("Neteisinga ivestis! Prasome ivesti skaiciu tarp 1 - 3!")
#
#
# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
#     while True:
#         print_board(board)
#         player_move(board, current_player)
#         if check_winner(board, current_player):
#             print(f"Zaidejas {current_player} laimejo!")
#             break
#         elif not get_free_positions(board):
#             print_board(board)
#             print('Lygiosios!')
#             break
#         current_player = '0' if current_player == 'X' else 'X'
#
#
# if __name__ == "__main__":
#     play_game()

#atspek skaiciu

# slaptas_skacius = random.randint(1,100)
# atspeta = False
#
# print ("Spekite skaiciu nuo 1 iki 100!")
# while not atspeta:
#     ivestis = input("Iveskite skaiciu_>")
#     try:
#         spejimas = int(ivestis)
#         if spejimas < slaptas_skacius:
#             print ("Per mazas skaicius !")
#         elif spejimas > slaptas_skacius:
#             print("Per didelis skaicius !")
#         else:
#             print("Sveikinaame! Atspejote skaiciu !")
#             atspeta = True
#     except ValueError:
#         print("Ivyko klaida: prasome ivesti skaiciu o ne raide ar kita simboli")

# def prideti_temperatura(temperaturos, miestas, temp):
#     if miestas in temperaturos:
#         temperaturos[miestas].append(temp)
#     else:
#         temperaturos[miestas] = [temp]
#
# def skaiciuoti_vidurki(temperaturos, miestas):
#     if miestas in temperaturos and len(temperaturos[miestas]) > 0:
#         return sum(temperaturos[miestas]) / len(temperaturos[miestas])
#     else:
#         return None
#
# def main():
#     temperaturos = {}
#
#     while True:
#         veiksmas = input("Pasirinkite veiksma: 'prideti' temperatura, 'vidurkis' miestui, arba 'baigti': ").lower()
#
#         if veiksmas == 'prideti':
#             miestas = input("Iveskite miesto pavadinima: ").capitalize()
#             try:
#                 temp = float(input("Iveskite temperatura: "))
#                 prideti_temperatura(temperaturos, miestas, temp)
#                 print(f"Temperatura prideta prie {miestas}.")
#             except ValueError:
#                 print("Klaida: Temperatura turi būti skaicius.")
#
#         elif veiksmas == 'vidurkis':
#             miestas = input("Iveskite miesto pavadinima, kurio vidurki norite suzinoti: ").capitalize()
#             vidurkis = skaiciuoti_vidurki(temperaturos, miestas)
#             if vidurkis is not None:
#                 print(f"{miestas} vidutine temperatura: {vidurkis:.2f}°C")
#             else:
#                 print(f"Nera duomenu apie {miestas} temperatura.")
#
#         elif veiksmas == 'baigti':
#             print("Programos darbas baigtas.")
#             break
#         else:
#             print("Klaida: Neteisingas veiksmas!")
#
# if __name__ == "__main__":
#     main()

#7 paskaita

# class Darbuotojas:
#     def __init__(self, vardas, atlyginimas):
#         self.vardas = vardas
#         self.atlyginimas = atlyginimas
#
#     def darbuotojo_informacija(self):
#         print(f"Darbuotojas: {self.vardas}, atlyginimas: {self.atlyginimas} EUR")
#
#
# class Vadovas(Darbuotojas):
#     def __init__(self, vardas, atlyginimas, padalinys):
#         super().__init__(vardas, atlyginimas)
#         self.padalinys = padalinys
#
#     def darbuotojo_informacija(self):
#         super().darbuotojo_informacija()
#         print(f"Padalinys: {self.padalinys}")
#
#
# darbuotojas = Darbuotojas('Jonas', 2000)
# vadovas = Vadovas('Petras', 3000, 'IT')
#
# darbuotojas.darbuotojo_informacija()
# vadovas.darbuotojo_informacija()

# class Variklis:
#     def __init__(self, galia):
#         self.galia = galia
#
#     def rodyti_galia(self):
#         print(f"Variklio galia: {self.galia} AG")
#
#
# class Automobilis(Variklis):
#     def __init__(self, marke, pagaminimo_metai, galia):
#         super().__init__(galia)
#         self.marke = marke
#         self.pagaminimo_metai = pagaminimo_metai
#
#     def informacija(self):
#         print(f"Marke: {self.marke}, \nPagaminimo metai: {self.pagaminimo_metai}")
#         super().rodyti_galia()
#
#
# variklis = Variklis(150)
# automobilis = Automobilis("Toyota", 2015, 250)
#
# automobilis.informacija()
# class Knyga:
#     def __init__(self, pavadinimas, autorius, metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.metai = metai
#
#     def info(self):
#         return f"{self.pavadinimas}, autorius: {self.autorius}, metai: {self.metai}"
#
#
# class MokslineKnyga(Knyga):
#     def __init__(self, pavadinimas, autorius, metai, sritis):
#         super().__init__(pavadinimas, autorius, metai)
#         self.sritis = sritis
#
#     def info(self):
#         return f"{super().info()}, sritis: {self.sritis}"
#
#
# class GrozineKnyga(Knyga):
#     def __init__(self, pavadinimas, autorius, metai, zanras):
#         super().__init__(pavadinimas, autorius, metai)
#         self.zanras = zanras
#
#     def info(self):
#         return f"{super().info()}, zanras: {self.zanras}"
#
#
# class Biblioteka:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#
#     def rodyti_knygas(self):
#         for knyga in self.knygos:
#             print(knyga.info())
#
#
# knyga1 = MokslineKnyga('Dirbtinis intelektas', "Petras Petraitis", 2020, 'Informatika')
# knyga2 = GrozineKnyga('Haris Poteris ir isminties akmuo', "J.K.Rowling", 1997, 'Fantastika')
#
# biblioteka = Biblioteka()
# biblioteka.prideti_knyga(knyga1)
# biblioteka.prideti_knyga(knyga2)
#
# biblioteka.rodyti_knygas()
# import csv
# class Preke:
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#
#     def info(self):
#         return f'{self.pavadinimas}, Kaina: {self.kaina}Eur'
#
#
# class Patiekalas(Preke):
#     def __init__(self, pavadinimas, kaina, paruosimo_laikas):
#         super().__init__(pavadinimas, kaina)
#         self.paruosimo_laikas = paruosimo_laikas
#
#     def info(self):
#         return f'{super().info()}, Paruosimo laikas: {self.paruosimo_laikas}min'
#
#
# class Gerimas(Preke):
#     def __init__(self, pavadinimas, kaina, turis):
#         super().__init__(pavadinimas, kaina)
#         self.turis = turis
#
#     def info(self):
#         return f'{super().info()}, Turis: {self.turis}ml'
#
#
# class Uzsakymas:
#     def __init__(self):
#         self.prekes = []
#
#     def prideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def apskaiciuoti_suma(self):
#         return sum(preke.kaina for preke in self.prekes)
#
#     def uzsakymo_info(self):
#         for preke in self.prekes:
#             print(preke.info())
#         print(f'Bendra suma: {self.apskaiciuoti_suma():.2f} Eur')
#
#
# class Restoranas:
#     def __init__(self):
#         self.uzsakymai = []
#         self.uzsakymo_id = 0
#
#     def prideti_uzsakyma(self, uzsakymas):
#         self.uzsakymo_id += 1
#         self.uzsakymai.append((self.uzsakymo_id, uzsakymas, 'Priimtas'))
#         print(f'Uzsakymo ID: {self.uzsakymo_id} priimtas!')
#
#     def atnaujinti_busena(self, uzsakymo_id, busena):
#         for uzsakymas in self.uzsakymai:
#             if uzsakymas[0] == uzsakymo_id:
#                 self.uzsakymai[self.uzsakymai.index(uzsakymas)] = (uzsakymo_id, uzsakymas[1], busena)
#                 print(f"Uzsakymo ID: {uzsakymo_id} busena atnaujinta i  ")
#                 break
#
#     def apskaiciuoti_saskaita(self, uzsakymo_id):
#         for uzsakymas in self.uzsakymai:
#             if uzsakymas[0] == uzsakymo_id:
#                 suma = uzsakymas[1].apskaiciuoti_suma()
#                 print(f"Uzsakymo ID: {uzsakymo_id} Saskaita: {suma:.2f} Eur")
#                 break
#
#     def rodyti_uzsakymus(self):
#         if not self.uzsakymai:
#             print("Siuo metu uzsakymu nera!")
#             return
#         for uzsakymas in self.uzsakymai:
#             print(f"Uzsakymo ID: {uzsakymas[0]}, busena: {uzsakymas[2]}")
#             uzsakymas[1].uzsakymo_info()
#             print('=' * 40)
#
#     def issaugoti_uzsakymus_csv(self, failo_pavadinimas):
#         with open(failo_pavadinimas, mode='w', newline='', encoding='utf-8') as failas:
#             writer = csv.writer(failas)
#             writer.writerow(["Uzsakymo ID", "Prekes pavaadinimaas", "Kaina", "Busena", "Paruosimo laikas", "Turis"])
#             for uzsakymas in self.uzsakymai:
#                 for preke in uzsakymas[1].prekes:
#                     paruosimo_laikas = preke.paruosimo_laikas if hasattr(preke, 'paruosimo_laikas') else ""
#                     turis = preke.turis if hasattr(preke, 'turis') else ""
#                     writer.writerow([uzsakymas[0], preke.pavadinimas, preke.kaina, uzsakymas[2], paruosimo_laikas, turis])
#
#     def ikelimas_is_csv(self, failo_pavadinimas):
#         with open(failo_pavadinimas, mode='r', newline='',encoding='utf-8') as failas:
#             reader = csv.DictReader(failas)
#             laikini_uzsakymai = {}
#             for eilute in reader:
#                 uzsakymo_id = int(eilute['Uzsakymo ID'])
#                 pavadinimas = eilute['Prekes pavadinimas']
#                 kaina = float(eilute['Kaina'])
#                 busena = eilute['Busena']
#                 paruosimo_laikas = eilute.get('Paruosimo laikas', "")
#                 turis = eilute.get('Turis', "")
#
#                 if paruosimo_laikas:
#                     preke = Patiekalas(pavadinimas, kaina,  int(paruosimo_laikas) if paruosimo_laikas.isdigit() else 0)
#                 elif turis:
#                     preke = Gerimas(pavadinimas, kaina, int(turis) if turis.isdigit() else 0)
#
#                 else:
#                     preke = Preke(pavadinimas, kaina)
#
#                 if uzsakymo_id not in laikini_uzsakymai:
#                     laikini_uzsakymai[uzsakymo_id] = Uzsakymas()
#                 laikini_uzsakymai[uzsakymo_id].prideti_preke(preke)
#
#                 self.atnaujinti_busena(uzsakymo_id, busena)
#             for uzsakymo_id in laikini_uzsakymai:
#                 self.prideti_uzsakyma(laikini_uzsakymai[uzsakymo_id])
#
#
#
#
#
#
# # sukuriam restorano objekta
#
#
#
# restoranas = Restoranas()
# # sukuriame keleta prekiu ir uzsakyma
# # pica = Patiekalas('Margarita', 11.99, 20)
# # alus = Gerimas('Tuborg', 1.29, 330)
# # uzsakymas = Uzsakymas()
# # uzsakymas.prideti_preke(pica)
# # uzsakymas.prideti_preke(alus)
# # # pridedam uzsakyma i restorana
# # restoranas.prideti_uzsakyma(uzsakymas)
# # # atnaujiname busena
# # restoranas.atnaujinti_busena(1, 'Paruostas')
# # # apskaiciuojame saskaita
# # restoranas.apskaiciuoti_saskaita(1)
# # # rodome visus uzsakymus
# restoranas.ikelimas_is_csv('uzsakymai.csv')
# restoranas.rodyti_uzsakymus()
# #
# # restoranas.issaugoti_uzsakymus_csv('uzsakymai.csv')

#GERAS:
# import csv
#
#
# class Preke:
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#
#     def info(self):
#         return f'{self.pavadinimas}, Kaina: {self.kaina}Eur'
#
#
# class Patiekalas(Preke):
#     def __init__(self, pavadinimas, kaina, paruosimo_laikas):
#         super().__init__(pavadinimas, kaina)
#         self.paruosimo_laikas = paruosimo_laikas
#
#     def info(self):
#         return f'{super().info()}, Paruosimo laikas: {self.paruosimo_laikas}min'
#
#
# class Gerimas(Preke):
#     def __init__(self, pavadinimas, kaina, turis):
#         super().__init__(pavadinimas, kaina)
#         self.turis = turis
#
#     def info(self):
#         return f'{super().info()}, Turis: {self.turis}ml'
#
#
# class Uzsakymas:
#     def __init__(self):
#         self.prekes = []
#
#     def prideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def apskaiciuoti_suma(self):
#         return sum(preke.kaina for preke in self.prekes)
#
#     def uzsakymo_info(self):
#         for preke in self.prekes:
#             print(preke.info())
#         print(f'Bendra suma: {self.apskaiciuoti_suma():.2f} Eur')
#
#
# class Restoranas:
#     def __init__(self):
#         self.uzsakymai = []
#         self.uzsakymo_id = 0
#
#     def prideti_uzsakyma(self, uzsakymas):
#         self.uzsakymo_id += 1
#         self.uzsakymai.append((self.uzsakymo_id, uzsakymas, 'Priimtas'))
#         print(f'Uzsakymo ID: {self.uzsakymo_id} priimtas!')
#
#     def atnaujinti_busena(self, uzsakymo_id, busena):
#         for uzsakymas in self.uzsakymai:
#             if uzsakymas[0] == uzsakymo_id:
#                 self.uzsakymai[self.uzsakymai.index(uzsakymas)] = (uzsakymo_id, uzsakymas[1], busena)
#                 print(f"Uzsakymo ID: {uzsakymo_id} busena atnaujinta i {busena} ")
#                 break
#
#     def apskaiciuoti_saskaita(self, uzsakymo_id):
#         for uzsakymas in self.uzsakymai:
#             if uzsakymas[0] == uzsakymo_id:
#                 suma = uzsakymas[1].apskaiciuoti_suma()
#                 print(f"Uzsakymo ID: {uzsakymo_id} Saskaita: {suma:.2f} Eur")
#                 break
#
#     def rodyti_uzsakymus(self):
#         if not self.uzsakymai:
#             print("Siuo metu uzsakymu nera!")
#             return
#         for uzsakymas in self.uzsakymai:
#             print(f"Uzsakymo ID: {uzsakymas[0]}, busena: {uzsakymas[2]}")
#             uzsakymas[1].uzsakymo_info()
#             print('=' * 40)
#
#     def issaugoti_uzsakymus_csv(self, failo_pavadinimas):
#         with open(failo_pavadinimas, mode='w', newline='', encoding='utf-8') as failas:
#             writer = csv.writer(failas)
#             writer.writerow(["Uzsakymo ID", "Prekes pavadinimas", "Kaina", "Busena", "Paruosimo laikas", "Turis"])
#             for uzsakymas in self.uzsakymai:
#                 for preke in uzsakymas[1].prekes:
#                     paruosimo_laikas = preke.paruosimo_laikas if hasattr(preke, 'paruosimo_laikas') else ""
#                     turis = preke.turis if hasattr(preke, 'turis') else ""
#                     writer.writerow(
#                         [uzsakymas[0], preke.pavadinimas, preke.kaina, uzsakymas[2], paruosimo_laikas, turis])
#
#     def ikelimas_is_csv(self, failo_pavadinimas):
#         with open(failo_pavadinimas, mode='r', newline='', encoding='utf-8') as failas:
#             reader = csv.DictReader(failas)
#             laikini_uzsakymai = {}
#             for eilute in reader:
#                 uzsakymo_id = int(eilute['Uzsakymo ID'])
#                 pavadinimas = eilute['Prekes pavadinimas']
#                 kaina = float(eilute['Kaina'])
#                 busena = eilute['Busena']
#                 paruosimo_laikas = eilute.get('Paruosimo laikas', "")
#                 turis = eilute.get('Turis', "")
#
#                 if paruosimo_laikas:
#                     preke = Patiekalas(pavadinimas, kaina, int(paruosimo_laikas) if paruosimo_laikas.isdigit() else 0)
#                 elif turis:
#                     preke = Gerimas(pavadinimas, kaina, int(turis) if turis.isdigit() else 0)
#                 else:
#                     preke = Preke(pavadinimas, kaina)
#
#                 if uzsakymo_id not in laikini_uzsakymai:
#                     laikini_uzsakymai[uzsakymo_id] = Uzsakymas()
#                 laikini_uzsakymai[uzsakymo_id].prideti_preke(preke)
#
#                 self.atnaujinti_busena(uzsakymo_id, busena)
#             for uzsakymo_id in laikini_uzsakymai:
#                 self.prideti_uzsakyma(laikini_uzsakymai[uzsakymo_id])
#
#
# class Meniu:
#     def __init__(self):
#         self.patiekalai = []
#         self.gerimai = []
#
#
#     def prideti_patiekala(self.patiekalas):
#         self.patiekalas.append(patiekalas)
#
#     def prideti_gerima(self.gerimas):
#         self.gerimas.append(gerima)
#
#     def rodyti_meniu(self):
#         print("Patiekalai:")
#         for patiekalas in self.patiekalai:
#             print(patiekalas)
#         print("\nGerimai:")
#         for gerimas in self.gerimai:
#             print(gerimas.info())
#
#     def rasti_patiekala(self, pavaadinimas):
#         for patiekalas in self.patiekalai:
#             if patiekalas.pavadinimas.lower() == pavadinimas.lower():
#                 return patiekalas
#         return None
#
#     def rasti_gerima(self, pavadinimas):
#         for gerimas in self.gerimai:
#             if gerimas.pavadinimas.lover() == pavadinimas.lower():
#                 return  gerimas
#         return None
#
# # sukuriam restorano objekta
# restoranas = Restoranas()
# restorano_meniu = Meniu()
#
# restorano_meniu.prideti_patiekala(pica)
# restorano_meniu.prideti_gerima(alus)
# # sukuriame keleta prekiu ir uzsakyma
# pica = Patiekalas('Margarita', 11.99, 20)
# alus = Gerimas('Tuborg', 1.29, 330)
# uzsakymas = Uzsakymas()
# uzsakymas.prideti_preke(pica)
# uzsakymas.prideti_preke(alus)
# # # pridedam uzsakyma i restorana
# restoranas.prideti_uzsakyma(uzsakymas)
# # # atnaujiname busena
# restoranas.atnaujinti_busena(1, 'Paruostas')
# # # apskaiciuojame saskaita
# restoranas.apskaiciuoti_saskaita(1)
# # rodome visus uzsakymus
#restoranas.rodyti_meniu()
# restoranas.issaugoti_uzsakymus_csv('uzsakymai.csv')


# 9 paskaita

from datetime import datetime
class Pranesimas:
    id_counter = 1
    def __init__(self, pranesimo_tekstas, autorius, publikavimo_data):
        self.id = Pranesimas.id_counter
        Pranesimas.id_counter +=1
        self.pranesimo_tekstas = pranesimo_tekstas
        self.autorius = autorius
        self.publikavimo_data = publikavimo_data

    def rodyti_informacija(self):
        print(f'pranesimo tekstas:{self.pranesimo_tekstas}')
        print(f'autorius:{self.autorius}')
        print(f'publikavimo data: {self.publikavimo_data.strftime("%Y-%m-%d %H:%M")}')

    def pakeisti_autoriu(self, naujas_autorius):
        self.autorius = naujas_autorius


class Komentarai(Pranesimas):
    def __init__(self, pranesimo_tekstas, autorius, publikavimo_data, komentaro_tekstas, pranesimo_ID):
        super(). __init__(pranesimo_tekstas, autorius, publikavimo_data)
        self.komentaro_tekstas = komentaro_tekstas
        self.pranesimo_ID = pranesimo_ID

    def rodyti_informacija(self):
        super().rodyti_informacija()
        print(f'komentaro tekstas:{self.komentaro_tekstas}')
        print(f'pranesimo ID:{self.pranesimo_ID}')



class PranesimuValdymas:
    def __init__(self):
        self.pranesimai = []
        self.komentarai = []


    def prideti_pranesima(self,pranesimas):
        self.pranesimai.append(pranesimas)

    def prideti_komentara(self, komentaras):
        self.komentarai.append(komentaras)

    def rodyti_pranesimus(self):
        for pranesimas in self.pranesimai:
            pranesimas.rodyti_informacija()
            print('\n---\n')

    def rodyti_komentarus(self, pranesimo_ID):
        for komentaras in self.komentarai:
            if komentaras.pranesimo_ID == pranesimo_ID:
                komentaras.rodyti_informacija()
                print('\n---\n')



class Blogas:
    def __init__(self):
        self.pranesimai =[]

    def prideti_pranesima(self, pranesimas):
        self.pranesimai.append(pranesimas)

    def pranesimai_su_zodis(self, zodis):
        rasti_pranesimai = []
        for pranesimas in self.pranesimai:
            if zodis in self.pranesimai.pranesimo_tekstas:
                rasti_pranesimai.append(pranesimas)

            if not rasti_pranesimai:
                print(f"Pranesimas su zodziu nerastas")
            else:
                for pranesimas in rasti_pranesimai
                    print(pranesimai.pranesimo_informacija)


    def istrinti_pranesima_pagal_ID (self, iD)
        for i, pranesimas in enumerate(self.pranesimai):
            if pranesimas.id == id:
                self.pranesimai.pop(i)
             return
        print("Pranesimas su nurodytu ID nerastas")



    def rodyti_pranesimus(self):
        for pranesimas in self.pranesimai:
            pranesimas.rodyti_informacija()
            print('\n---\n')


    # def istrinti_pranesimaID(self):
    #     for pranesimas in self.pranesimai:
    #         if pranesimo_ID == 1
    #             pranesimas.remove(pranesimas)
    #             except ValueError:
    #             print("Pranesimo su tokiu ID nera")


class Forumas:
    def __init__(self):
        self.komentarai = []

    def prideti_komentara(self, komentarai):
        self.komentarai.append(komentaras)

    # def rasti_komentra_su_max_balsiu(self):
    #     for komentaras in self.komentarai:
    #         if

    def rodyti_komentarus(self, iD):
        for komentaras in self.komentarai:
            if komentaras.pranesimo_ID == pranesimo_ID:
                komentaras.rodyti_informacija()
                print('\n---\n')


def main():
    valdymas = PranesimuValdymas()
    while True:
        print("\n1. Prideti pranesima")
        print("2. Prideti komentara")
        print("3. Rodyti pranesimus")
        print("4. Balsuoti uz komentara")
        print("5. Iseiti")

        veiksmas = input("Pasirinkinte veiksmaa_>")
        if veiksmas = '1'
            tekstas = input("Iveskite pranesimo teksta_>")
            autorius = input("Iveskite autoriaus varda")
            valdymas.prideti_pranesima(tekstas, autorius)
        elif veiksmas = '2'
            tekstas = input("Iveskite komentaro teksta_>")
            autorius = input("Iveskite autoriaus varda")
            valdymas.prideti_komentra(tekstas)
        elif veiksmas = '3'

#valdymas = PranesimuValdymas()

# blogas = Blogas()
#
#
#
# publikavimo_data = datetime.now()
# pranesimas = Pranesimas("Labas pasauli", "Jonas", publikavimo_data)
# #valdymas.prideti_pranesima(pranesimas)
# blogas.prideti_pranesima(pranesimas)
#
# #pranesimas.rodyti_informacija()
#
# print("\n---\n")
#
# #komentaras = Komentarai("Labas pasauli", "Jonas", publikavimo_data, "Puikus straipsnis", 1)
# #valdymas.prideti_komentara(komentaras)
#
# #valdymas.rodyti_pranesimus()
# #valdymas.rodyti_komentarus(1)
#
# blogas.rodyti_pranesimus()
# blogas.pranesimai_su_zodis()
#
# #komentaras.rodyti_informacija()







