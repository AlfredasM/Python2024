import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv('automobiliai.csv')

#print(df)

brangiausia_marke = df.groupby('Markė')['Kaina'].max().sort_values(ascending=False).head(1)

#print(brangiausia_marke)


vidutine_kaina_pagal_marke = df.groupby('Markė')['Kaina'].mean().sort_values(ascending=True).round(2)

#print(vidutine_kaina_pagal_marke)



dazniausiai_pasitaikancius_metus = df['Metai'].mode()[0]

#print(dazniausiai_pasitaikancius_metus)



kainu_min_max_tarp_markiu = df.groupby('Markė')['Kaina'].agg(['min','max'])

#print(kainu_min_max_tarp_markiu)



automobiliu_pasiskirstymas_pagal_metus = df['Metai'].value_counts().sort_index()

#print(automobiliu_pasiskirstymas_pagal_metus)



brangiausiu_modeliu_penktetukas = df.sort_values(by='Kaina', ascending=False).head(5)[['Markė','Modelis','Kaina']].reset_index(drop=True)

#print(brangiausiu_modeliu_penktetukas)



automobiliu_skaicius_pagal_marke = df['Markė'].value_counts()

#print(automobiliu_skaicius_pagal_marke)



vidutine_kaina_pagal_metus = df.groupby('Metai')['Kaina'].mean().sort_values(ascending=False).round(2)

print(vidutine_kaina_pagal_metus)



metu_ir_kainos_koreliacija = df[['Metai', 'Kaina']].corr()

#print(metu_ir_kainos_koreliacija)


# df['Skaitymo trukme val.'] = df['Puslapiu sk'] / 100

#print(df)

vidutiniskai_psl_zanre = df.groupby('Zanras')['Puslapiu sk'].mean()

#print(vidutiniskai_psl_zanre)

daugiau_negu_300 = df[df['Puslapiu sk'] > 300]

# # vyresni_nei_30 = df[df['Amzius'] > 30]
# # print(vyresni_nei_30)