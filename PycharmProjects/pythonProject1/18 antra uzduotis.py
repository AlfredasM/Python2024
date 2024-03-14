# 1. Nustatykite, kiek darbuotojų dirba kiekviename skyriuje (DEPARTMENT_ID).
# 2. Apskaičiuokite vidutinį atlyginimą (SALARY) kiekvienai darbo pozicijai (JOB_ID).
# 3. Remiantis HIRE_DATE, nustatykite, kiek laiko vidutiniškai darbuotojai dirba įmonėje.
# 4. Sukurkite histogramą, vaizduojančią atlyginimų (SALARY) pasiskirstymą įmonėje.
# 5. Analizuokite, kaip įdarbinimo data (HIRE_DATE) pasiskirsto per metus, ir nustatykite,
# kuriais metais buvo priimta daugiausiai darbuotojų.
import pandas as pd
from matplotlib import pyplot as plt

emplo = "employees.csv"
df = pd.read_csv(emplo)
#print(df)

#darbuotojai_kieviename_skyriuje = df('DEPARTMENT_ID')['EMPLOYEE_ID'].count()

#print(darbuotojai_kieviename_skyriuje)

vidutinis_atlyginimas_kiekvienai_darbo_pozicijai = df.groupby('JOB_ID')['SALARY'].mean().sort_values(ascending=True)

#print(vidutinis_atlyginimas_kiekvienai_darbo_pozicijai)

df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'], format='%d-%b-%y')


df['Darbo_stazas'] = (pd.to_datetime('today') - df['HIRE_DATE']).dt.days / 365.25
vidutinis_darbo_stazas = df['Darbo_stazas'].mean().round(2)

print(vidutinis_darbo_stazas)

#vidutinis_darbuotojo_isdirbtas_laikas = df.groupby('EMPLOYER_ID')['YEAR']


plt.figure(figsize=(12, 8))
vidutinis_atlyginimas_kiekvienai_darbo_pozicijai.plot(kind='bar', color='green')
plt.title('Atlyginimu pasiskirtymas pagal darbo pozicijas')
plt.xlabel('Departmen')
plt.ylabel('Average solary')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


rysys_tarp_skyriaus_ir_atlyginimo_koreliacija = df[['DEPARTMENT_ID', 'SALARY']].corr()

#print(rysys_tarp_skyriaus_ir_atlyginimo_koreliacija)


df['Hire_YEAR'] = df['HIRE_DATE'].dt.year
darbuotojai_pagal_metus = df.groupby('Hire_YEAR').size()

plt.figure(figsize=(10, 6))
darbuotojai_pagal_metus.plot(kind='bar', color='red')
plt.title('Idarbinimas pagal metus')
plt.xlabel('Metai')
plt.ylabel('Darbuotoju skaicius')
plt.show()


vidutinis_atlyginimas_departamentui = df.groupby('DEPARTMENT_ID')['SALARY'].mean().sort_values(ascending=True)

print(vidutinis_atlyginimas_departamentui)

plt.figure(figsize=(12, 8))
vidutinis_atlyginimas_departamentui.plot(kind='bar', color='green')
plt.title('Atlyginimu pasiskirtymas pagal departamenta')
plt.xlabel('Departmen')
plt.ylabel('Average solary')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()