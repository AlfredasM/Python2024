import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv('os_worldwide.csv')


#print(df)


# plt.figure(figsize=(10, 6))
# plt.plot(df['Date'], df['Windows'], marker='o', color='r', label = 'Windows')
# plt.plot(df['Date'], df['Android'], marker='o', color='b', label = 'Android')
# plt.plot(df['Date'], df['iOS'], marker='o', color='y', label = 'iOS')
#
# plt.xlabel('Metai')
# plt.ylabel('Pokytis')
# plt.title("Populiariausiu sistemu pokytis per laikotrarpi")
# plt.show()



#kaip_keitesi_per_laikotrapi_WIND_ANDR_IOS =
#2

4#
#duomenys_pagal_metus = df.groupby('Date')['Windows']


#print(duomenys_pagal_metus)
5#
#os_data['Month'] = os_data['Data'].dt.month

#sezoniskumas_pagal_menesi = (os_data.groupby('M'))


#6

# os_data['Date'] = pd.to_datetime(os_data['Date'])
#
# os_data['Month'] = os_data['Date'].dt.month
#
# sezoniniskumas_pagal_menesi = (os_data.groupby('Month')
#                                .agg({'Windows': 'mean', 'Android': 'mean', 'iOS': 'mean'}))
#
# plt.figure(figsize=(14, 8))
# for os_name in ['Windows', 'Android', 'iOS']:
#     plt.plot(sezoniniskumas_pagal_menesi.index,
#              sezoniniskumas_pagal_menesi[os_name], label=os_name, marker='o')
#     plt.title('Sezoniskumas Pagal menesi Windows, Android ir iOS')
#     plt.xlabel('Menuo')
#     plt.ylabel('Vidutine menesine rinkos dalis (%)')
#     plt.legend()
#     plt.grid(True)
#     plt.xticks(range(1, 13), ['Sausis','Vasaris','Kovas','Balandis','Geguze',
#                               'Birzelis','Liepa','Rugpjutis','Rugsejis','Spalis','Lapkritis','Gruodis'])
# plt.show()



rinkos_pagal_windows = df.groupby('Date')['Windows'].mode()


print(rinkos_pagal_windows)


#print(windows_itaka_android)

# laikotarpis_wind_ir_andr_virsyjo30proc =df[df['Windows'] > 30]

#print(laikotarpis_wind_ir_andr_virsyjo30proc)