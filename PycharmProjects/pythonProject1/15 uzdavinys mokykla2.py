# Sukurkite mokyklos bibliotekos knygų duomenų rinkinį, kuriame saugoma informacija apie knygas, jų žanrus, puslapių skaičių,
# ir ar knyga yra skolinama. Jūsų užduotis – atlikti duomenų analizę ir vizualizaciją, naudojant pandas ir matplotlib.

#     * Sukurkite naują stulpelį Skaitymo trukmė (val), kuris apskaičiuotų, kiek vidutiniškai laiko (valandomis) užtruktų
# perskaityti knygą, jei žmogus skaitytų 100 puslapių per valandą.

#     * Apskaičiuokite, kiek vidutiniškai puslapių turi knyga kiekviename žanre.

#     * Filtruokite ir atspausdinkite tik tas knygas, kurios yra skolinamos ir turi daugiau nei 300 puslapių.

#     * Naudodami matplotlib, nubrėžkite stulpelinę diagramą, kurioje vaizduojamas knygų skaičius kiekviename žanre. (Nebūtina)

import pandas as pd

data = {
    'Pavadinimas':['Poteris','Sniego karaliene','Kliudziau','Enciklopedija'],
    'Zanras':['Fantastika','Siaubo','Siaubo','Moksline'],
    'Puslapiu sk':[150, 250, 350, 400],
    'Skolinamos':['Taip','Ne','Taip','Ne']
}

df = pd.DataFrame(data)

# df['Skaitymo trukme val.'] = df['Puslapiu sk'] / 100

#print(df)

vidutiniskai_psl_zanre = df.groupby('Zanras')['Puslapiu sk'].mean()

#print(vidutiniskai_psl_zanre)

daugiau_negu_300 = df[df['Puslapiu sk'] > 300]

# # vyresni_nei_30 = df[df['Amzius'] > 30]
# # print(vyresni_nei_30)




print(daugiau_negu_300)

