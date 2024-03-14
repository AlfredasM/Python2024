



# 5. Išanalizuokite, kaip keitėsi pardavimai per mėnesį. Tam reikės sugrupuoti duomenis pagal mėnesį ir
# apskaičiuoti bendrą pardavimų sumą kiekvienam mėnesiui.
import pandas as pd

data = 'prekybos_duomenys.csv'
df = pd.read_csv(data)
# 1. Apskaičiuokite, kiek bendrai buvo uždirbta iš kiekvieno produkto. Tai padės identifikuoti labiausiai pelningus produktus.
# pelningiausi_produktai = df.groupby('Produktas')['Pardavimai'].sum()
# print(pelningiausi_produktai)

df['date'] = pd.to_datetime(df['Data'])
df['metai_menuo'] = df['date'].dt.to_period('M')
# 2. Konvertuokite Data stulpelį į datos formatą ir apskaičiuokite, kiek vidutiniškai buvo uždirbta per mėnesį.
pardavimai_per_menesi = df.groupby('metai_menuo')['Pardavimai'].mean().round(2)
print(pardavimai_per_menesi)

# 3. Nustatykite, kurių produktų buvo parduota daugiausiai vienetų.
# daugiausia_parduota_vnt = df.groupby('Produktas')['Kiekis'].max().sort_values(ascending=False).head(5)
# print(daugiausia_parduota_vnt)

# 4. Atrinkite dešimt didžiausių pardavimų pagal sumą.

df['suma_pardavimo'] = df['Pardavimai'] / df['Kiekis']

didziausiu_pardavimu_10 = df.sort_values('suma_pardavimo',ascending=False).head(10).round(2)
print(didziausiu_pardavimu_10)

# maziausiai_parduota_10 = df.groupby('Produktas')['Pardavimai'].sum().sort_values(ascending=True).head(10)
# print(maziausiai_parduota_10)

# keitesi_per_menesi = df.groupby('month')['Pardavimai'].sum().sort_values(ascending=False)
# print(keitesi_per_menesi)



