import pandas as pd
import matplotlib.pyplot as plt

# data = {
#     'Vardas':['Antanas', 'Petras', 'Ona', 'Ieva', 'Julija'],
#     'Amzius':[28, 34, 19, 42, 27],
#     'Miestas':['Vilnius','Alytus','Ariogala', 'Klaipeda','Klaipeda']
# }
# df = pd.DataFrame(data)
#
# #print(df['Amzius'])
#
#
# #print(df[['Vardas','Amzius']])
#
#
# # vyresni_nei_30 = df[df['Amzius'] > 30]
# # print(vyresni_nei_30)
#
#
# # df['Vyresni nei 30'] = df['Amzius'] > 30
# # print(df)
#
#
# #rusiavimas
# # df_sorted = df.sort_values(by='Amzius', ascending=True)
# # print(df_sorted)
#
# #rusiavimas
# # df_sorted = df.sort_values(by=['Miestas', 'Amzius'])
# # print(df_sorted)
#
#
# #grupavimas (vidurkis <mean>)
# # grouped_df = df.groupby('Miestas')['Amzius'].mean()
# # print(grouped_df)


# data = {
#     'Renginio data': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-05-02'],
#     'Miestas': ['Vilnius', 'Alytus', 'Kaunas', 'Kaunas'],
#     'Dalyviai':[300, 150, 200, 300]
# }
#
# df = pd.DataFrame(data)
# #print(df)
#
# def renginio_dydis(dydis):
#     if dydis < 125:
#         return 'Mazas'
#     elif 125 <= dydis <= 200:
#         return 'Vidutinis'
#     else:
#         return 'Didelis'
#
# df['Renginio dydis'] = df['Dalyviai'].apply(renginio_dydis)
#
# print(df)
#
# bendras_dalyviu_skaicius_mieste = df.groupby('Miestas')['Dalyviai'].sum()
#
# print(bendras_dalyviu_skaicius_mieste)







# Sukurkite dataframe su stulpeliais [Šalis, Gyventojų skaičius mln, BVP, mlrd. USD]
#
# Pridėkite naują stulpelį BVP vienam gyventojui, USD, kuris apskaičiuojamas padalinant BVP iš gyventojų skaičiaus ir padauginant iš milijono.
# Raskite ir atspausdinkite šalį su didžiausiu BVP vienam gyventojui.
# Pridėkite naują stulpelį Ekonomikos kategorija, kuris kategorizuoja šalis pagal jų BVP:
#         * Jei BVP mažesnis nei 100 mlrd. USD, Ekonomikos kategorija yra 'Maža ekonomika'.
#         * Jei BVP yra tarp 100 mlrd. USD ir 1000 mlrd. USD, Ekonomikos kategorija yra 'Vidutinė ekonomika'.
#         * Jei BVP didesnis nei 1000 mlrd. USD, Ekonomikos kategorija yra 'Didelė ekonomika'.
# Grupuokite duomenis pagal Ekonomikos kategorija ir apskaičiuokite vidutinį BVP vienam gyventojui kiekvienoje kategorijoje.

# data = {
#     'Salis':['Lietuva','Ispanija','Italija', 'Vokietija','Anglija'],
#     'Gyventoju skaicius mln.':[3, 10, 15, 20, 12],
#     'BVP mlrd.USD':[86, 200, 900, 400, 500]
#
# }
# df = pd.DataFrame(data)
#
# df['BVP vienam gyventojui, USD'] = (df['BVP mlrd.USD'] *1e9) / (df['Gyventoju skaicius mln.'] * 1e6)

#print(df)

# didziausias_BVP_vienam_gyventojui = df[df['BVP vienam gyventojui, USD'] == df['BVP vienam gyventojui, USD'].max()]['Salis']

#print(f'Didziausias BVP vienam gyventojaui yra: {didziausias_BVP_vienam_gyventojui.iloc[0]}')


# def ekonomikos_kategorija(bvp):
#     if bvp < 100:
#         return 'Maza ekonomika'
#     elif 100 <= bvp <= 1000:
#         return 'Vidutine ekonomika'
#     else:
#         return 'Didele ekonomika'
#
#
# df['Ekonomikos kategorija'] = df['BVP mlrd.USD'].apply(ekonomikos_kategorija)
#
# #print(df)
#
# vidutinis_BVP_vienam_gyventojui = df.groupby('Ekonomikos kategorija')['BVP vienam gyventojui, USD'].mean().reset_index()
#
# #print(vidutinis_BVP_vienam_gyventojui)
#
# plt.figure(figsize=(10,6))
# plt.bar(vidutinis_BVP_vienam_gyventojui['Ekonomikos kategorija'], vidutinis_BVP_vienam_gyventojui['BVP vienam gyventojui, USD'], color='skyblue')
#
# plt.title('Vidutinis BVP vienam gyventojui pagal ekonomikos kategorija')
# plt.xlabel('Ekonomikos kategorija', fontsize=20)
# plt.ylabel('BVP vienam gyventojui, USD')
# #plt.xticks(rotation=25)
# plt.show()
