import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Valiutosbankas.csv')
print(df)

df['Santykis'] = df['Santykis'].str.replace(' ', '').str.replace(',', '.').astype(float)
df['Pokytis vnt.'] = df['Pokytis vnt.'].str.replace(',', '.').astype(float)
df['Pokytis %'] = df['Pokytis %'].str.replace(',', '.').str.replace('%', '').astype(float)

vidutiniai_ikainiai = df.groupby('Valiutos kodas').agg({'Santykis': 'mean', 'Pokytis %': 'mean'}).reset_index()
vidutiniai_ikainiai.rename(columns={'Santykis': 'Vidutinis santykis', 'Pokytis %': 'Vidutinis pokytis %'}, inplace=True)
# print(vidutiniai_ikainiai)

valiutos = ['USD', 'DKK', 'ISK']
isfiltruota = df[df['Valiutos kodas'].isin(valiutos)]
# print(isfiltruota)

plt.figure(figsize=(14,7))
for valiuta in valiutos:
    valiutos_duomenys = isfiltruota[isfiltruota['Valiutos kodas']==valiuta]
    plt.plot(valiutos_duomenys['Data'], valiutos_duomenys['Santykis'], label=valiuta)
plt.title('Valiutu santykio trendai')
plt.xlabel('Data')
plt.ylabel('Sanktykis')
plt.legend()
# plt.show()

didziausi_pasikeitimai = df.loc[df.groupby('Valiutos kodas')['Pokytis %'].idxmax()]       #randa didziausia pasikeitima idxmax
didziausi_pasikeitimai = didziausi_pasikeitimai[['Valiutos kodas', 'Pokytis %', 'Data']]
# print(didziausi_pasikeitimai)

maziausi_pasikeitimai = df.loc[df.groupby('Valiutos kodas')['Pokytis %'].idxmin()].reset_index()      #randa maziausia pasikeitima idxmin
maziausi_pasikeitimai = maziausi_pasikeitimai[['Valiutos kodas', 'Pokytis %', 'Data']]
# print(maziausi_pasikeitimai)

pivot_data = df.pivot(index='Data', columns='Valiutos kodas', values='Pokytis %')
koreliacijos_matrica = pivot_data.corr()
# print(koreliacijos_matrica)
max_koreliacijos_reiksme = koreliacijos_matrica.max().max()
print(koreliacijos_matrica)