# Sukurkite duomenų rinkinį, kuriame saugoma informacija apie įvairių knygų pardavimus per metus. Duomenys apima knygos pavadinimą,
# autorių, pardavimų skaičių ir išleidimo metus.
#     * Raskite, kiek vidutiniškai buvo parduota knygų kiekvieno autoriaus.
#     * Sukurkite naują stulpelį 'Amžius', kuriame būtų nurodyta, kiek metų knygai nuo jos išleidimo iki 2024 metų.
#     * Apskaičiuokite, kuri knyga buvo parduota geriausiai kiekvieno autoriaus atžvilgiu. (Praleiskite)
#     * Grupuokite duomenis pagal išleidimo metus ir apskaičiuokite, kiek knygų buvo išleista kiekvienais metais.

import pandas as pd

data = {
    'Pavadinimas':['Alchemikas', 'Kliudziau', 'Milijonas', 'Enciklopedija'],
    'Autorius':['Petras Petraitis','Jonas Jonaitis', 'Jonas Jonaitis','Maryte Marytaite'],
    'Pardavimu skaicius':[10, 120, 30, 40],
    'Metai':['2001', '2001', '1956', '1956']

}

df = pd.DataFrame(data)

grouped_df = df.groupby('Autorius')['Pardavimu skaicius'].mean()

#print(grouped_df)

#df['Knygos amzius nuo 2024'] = 2024 - df['Metai']

#print(df)


max_pardavimai = df.groupby('Autorius')['Pardavimu skaicius'].transform('max') == df['Pardavimu skaicius']
geriausiai_parduotos_knygos = df [max_pardavimai]

print(geriausiai_parduotos_knygos[['Autorius', 'Pavadinimas', 'Pardavimu skaicius']])

grupuoti_pagal_isleidimo_metus = df.groupby('Metai').size()



print(grupuoti_pagal_isleidimo_metus)






