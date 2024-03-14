import pandas as pd

# klientai1 = pd.DataFrame({
#     'klientoID': [1, 3, 5, 7],
#     'vardas': ['Petras', 'Jonas', 'Zigmas', 'Antanas'],
#     'pavarde': ['Petraitis', 'Jonaitis', 'Zigmaitis', 'Antanaitis']
# })
#
# klientai2 = pd.DataFrame({
#     'klientoID': [2, 4, 6, 8],
#     'vardas': ['Onute', 'Maryte', 'Ieva', 'Natasha'],
#     'pavarde': ['Onutaite', 'Marytaite', 'Ievaite', 'Natasaite']
# })
#
# concatenated = pd.concat([klientai1, klientai2], axis=0)

#print(concatenated)
#
# pardavimai3 =pd.DataFrame({
#     'klientoID': [1, 2, 3, 5],
#     'pardavimoID': [8, 9, 11, 3],
#     'suma': [400, 500, 2000, 3000]
# })
# klientai3 =pd.DataFrame({
#     'klientoID': [1, 2, 3, 4],
#     'vardas': ['Petras', 'Jonas', 'Zigmas', 'Antanas'],
#     'pavarde': ['Petraitis', 'Jonaitis', 'Zigmaitis', 'Antanaitis']
# })
#
# merged = pd.merge(pardavimai3, klientai3, on='klientoID', right_index=False)
#
# print(merged)
#=======================================================================
# produktaiduomeys = pd.DataFrame({
#     'produktasID': [2, 4, 6, 8],
#     'pavadinimas': ['duona', 'pienas', 'sviestas', 'suris'],
#     'kaina': [5, 3, 4, 10 ]
# })
# pardavimaiduomenys = pd.DataFrame({
#     'pardavimoID': [11, 12, 13, 14],
#     'produktasID': [2, 4, 6, 8],
#     'parduota_vnt': [50, 200, 25, 30]
# })
# produktaiduomenys.set_index('produktasID', inplace=True)
# joined_produktasID = pardavimaiduomenys.join(produktaiduomeys, on='produktasID')
#
# print(joined_produktasID)
#====================================================================
# klientuduomenys = pd.DataFrame({
#     'klientoID': [11, 12, 13, 14, 11],
#     'vardas': ['Petras', 'Jonas', 'Zigmas', 'Antanas','Petras'],
#     'pavarde': ['Petraitis', 'Jonaitis', 'Zigmaitis', 'Antanaitis','Petraitis'],
#     'elpastas': ['petras@gmail.com','jonas@gmail.com', 'zigmas@gmail.com', 'antanas@gmail.com','petras@gmail.com']
#
# })
#
# klientuduomenys_be_dublikatu = klientuduomenys.drop_duplicates(subset=['elpastas'])
#
# print(klientuduomenys_be_dublikatu)
#=====================================================================

pardavimai = pd.DataFrame({
    'pardavimoID': [11, 12, 13, 14],
    'klientoID': [1, 2, 3, 4],
    'produktoID': [2, 4, 6, 8],
    'pardavimosuma': [50, 30, 400, 100]
})
filtruoti_pardavimai = pardavimai[pardavimai['pardavimosuma'] >= 100]

print(filtruoti_pardavimai)

pasalinti_stulpeli = filtruoti_pardavimai.drop(columns=['klientoID'])
print(pasalinti_stulpeli)
# be_klientoID =pardavimai.drop('klientoID', axis=1)
#
# pardavimai['suma_virsyja100'] = be_klientoID['pardavimosuma'] >= 100
#
# print(pardavimai)



#print(suma_virsyja100)