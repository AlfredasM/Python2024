# 1. Analizuokite duomenų rinkinį, kad nustatytumėte 5 labiausiai parduodamus žaidimus visame pasaulyje.
# Atsižvelkite į pardavimų skaičius ir platformas, ant kurių šie žaidimai yra.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')

pardavimai_pasaulyje_TOP5 = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(5)
#print(pardavimai_pasaulyje_TOP5)

# 2.Ištirkite duomenų rinkinį, kad nustatytumėte, kaip keitėsi video žaidimų pardavimai per metus.
# Susitelkite į pasaulinių pardavimų tendencijas nuo 2000 metų iki dabar.

metai_nuo2000 = df[df['Year'] > 2000]

pardavimai_pagal_metus = df.groupby('Year')['Global_Sales'].sum()


plt.figure(figsize=(14, 7))
pardavimai_pagal_metus.plot(kind='bar', color='red')
plt.ylabel('Pardavimai')
plt.show()

#3.Analizuokite duomenis, kad sužinotumėte, kuris žaidimų žanras buvo populiariausias pagal pasaulinius pardavimus.
# Palyginkite tris populiariausius žanrus.

populiariausias_zanras_pagal_pardavimus = df.groupby('Genre')['Global_Sales'].sum().head(3)

#print(populiariausias_zanras_pagal_pardavimus)

#4. Apskaičiuokite 5 pagrindinių leidėjų rinkos dalį pagal pasaulinius pardavimus.
# Atsižvelkite, kaip šios dalys keitėsi per paskutinį dešimtmetį.


import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)

# Analizuokite duomenų rinkinį, kad nustatytumėte 5 labiausiai parduodamus žaidimus visame pasaulyje.
# Atsižvelkite į pardavimų skaičius ir platformas, ant kurių šie žaidimai yra.
df = pd.read_csv('21-vgsales.csv')
df['Year'] = df['Year'].fillna(0).astype(int)

daugiausia_parduodama = df.sort_values('Global_Sales', ascending=False).head(5)
print(f'Daugiausiai parduodamu zaidimu top 5:\n, {daugiausia_parduodama}')

# Ištirkite duomenų rinkinį, kad nustatytumėte, kaip keitėsi video žaidimų pardavimai per metus.
# Susitelkite į pasaulinių pardavimų tendencijas nuo 2000 metų iki dabar.
metiniai_pardavimai = df[df['Year'] >= 2000].groupby('Year')['Global_Sales'].sum()
print(f'Zaidimu pardavimai kiekvienais metais:\n {metiniai_pardavimai}')

plt.figure(figsize=(10, 6))
plt.plot(metiniai_pardavimai)
plt.title('Žaidimų pardavimo tendencijos 2000-2020 m.')
plt.xlabel('Metai')
plt.ylabel('Suma, mln.$')
plt.xticks([2000, 2005, 2010, 2015, 2020])
plt.show()

# 3. Analizuokite duomenis, kad sužinotumėte, kuris žaidimų žanras buvo populiariausias pagal pasaulinius pardavimus.
# Palyginkite tris populiariausius žanrus.
pop_zanras = df.groupby('Genre')['Global_Sales'].sum().head(3)
print(f'3 populiariausi žaidimų žanrai: \n{pop_zanras}')

# Apskaičiuokite 5 pagrindinių leidėjų rinkos dalį pagal pasaulinius pardavimus.
# Atsižvelkite, kaip šios dalys keitėsi per paskutinį dešimtmetį.
total_sales = df['Global_Sales'].sum()
top5_leidejai = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(5).div(total_sales)
print(f'\nTop 5 leidjų rinkos dalis: \n{top5_leidejai}')

recent_data = df[df['Year'] >= (df['Year'].max() - 10)]
print('-' * 80)

leidejo_sales = recent_data.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(5)
print(f'Leidejo visi pardavimai per 10 m: \n {leidejo_sales}')
leideju_total = recent_data['Global_Sales'].sum()
leidejo_market_share = (leidejo_sales / leideju_total) * 100
print(f'5 leideju rinkos dalis per paskutinį dešimtmetį {leidejo_market_share}')