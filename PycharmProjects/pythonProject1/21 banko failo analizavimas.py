import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Valiutosbankas.csv')

#print(df)

#print(df)
df['Santykis'] = df['Santykis'].str.replace(' ', '').str.replace(',', '.').astype(float)
df['Pokytis vnt.'] = df['Pokytis vnt.'].str.replace(',', '.').astype(float)
df['Pokytis %'] = df['Pokytis %'].str.replace(',', '.').str.replace('%', '').astype(float)

#print(df)
average_rates = df.groupby('Valiutos kodas').agg({'Santykis': 'mean', 'Pokytis %': 'mean'}).reset_index()
average_rates.rename(columns={'Santykis': 'Vidutinis santykis', 'Pokytis %': 'Vidutinis Pokytis %'}, inplace=True)
print(average_rates)


# valiutos = ['ISK']
#
# filter_data = df[df['Valiutos kodas'].isin(valiutos)]
#
# #print(filter_data)
#
# plt.figure(figsize=(14, 7))
# for valiuta in valiutos:
#     valiutos_data = filter_data[filter_data['Valiutos kodas']==valiuta]
#     plt.plot(valiutos_data['Data'], valiutos_data['Santykis'], label=valiuta)
# plt.title('Valiutu santykio trendai')
# plt.xlabel('Data')
# plt.ylabel('Santykis')
# plt.legend()
# #plt.show()

# didziausi_pasikeitimai = df.loc[df.groupby('Valiutos kodas')['Pokytis %'].idxmax()]       #randa didziausia pasikeitima idxmax
# didziausi_pasikeitimai = didziausi_pasikeitimai[['Valiutos kodas', 'Pokytis %', 'Data']]
# # print(didziausi_pasikeitimai)
#
# maziausi_pasikeitimai = df.loc[df.groupby('Valiutos kodas')['Pokytis %'].idxmin()].reset_index()      #randa maziausia pasikeitima idxmin
# maziausi_pasikeitimai = maziausi_pasikeitimai[['Valiutos kodas', 'Pokytis %', 'Data']]
# #print(maziausi_pasikeitimai)

# pivot_data = df.pivot(index='Data', columns='Valiutos kodas', values='Pokytis %')
# koreliacijos_matrica = pivot_data.corr()
#
#
# max_koreliacijos_reiksme = koreliacijos_matrica.max().max()
#
# print(koreliacijos_matrica)


# 2. Palyginkite skirtingų valiutų pasikeitimus per laikotarpį,
# apskaičiuodami kiekvienos valiutos vidutinius keitimo kursus ar pokyčius.

vidutiniai_valiutu_keitimo_kursai = df.groupby('Valiutos kodas')['Santykis'].mean()
#print(vidutiniai_valiutu_keitimo_kursai)