import pandas as pd
#
# df = pd.DataFrame({
#     'date_str': ['2020-05-01', '2020-05-21', '2021-07-29']
# })
# """
# pakeisti is teksto i datu foemata, patikrinti koks formatas
# """
# df['date'] = pd.to_datetime(df['date_str'])
# # print(df)##konverojam is teksto i tikras datas
# df_info = df.dtypes #patikriname koks datos tipas, ar str(tekstas) ar tikra data
# # print(df_info)
# """
# skirstymas pagal metus, men ir dienas
# """
# df['year'] = df['date'].dt.year #isskiriams pagal metus, menesius ar dienas
# df['month'] = df['date'].dt.month
# df['day'] = df['date'].dt.day
#
# # print(df[['date', 'year', 'month', 'day']])
# """
# paprasyti atspausdinti dienomis ar savaitemis
# """
# date_range_daily = pd.date_range(start='2020-03-01', end='2024-03-07', freq='D') #freq su raide D - kokiu daznumu, pvz Dienomis kasdien
# date_range_daily_list = date_range_daily.strftime('%Y-%m-%d').tolist()
# # print(f'Daily date range: {date_range_daily}')
# # print(f'Daily date range: {date_range_daily_list}')
#
# """
# Pritaikymas laiko juostai
# """
# date_range_weekly = pd.date_range(start='2024-03-01', periods=4, freq='W') ## 4- reiskia, kad norime sukurti 4 datas
# # print(f'Weekly date range: {date_range_weekly}')
#
# df['date_utc'] = df['date'].dt.tz_localize('UTC') #kai norim pritaikyti prie laiko juostos
# # tz- time zone, priskyria nurodyta laiko juosta, pvz "UTC' - "Universal time coordinetor"
#
# df['date_eastern'] = df['date_utc'].dt.tz_convert('US/Eastern')
# print(df[['date_utc', 'date_eastern']])
#
# """
# datos formato pakeitimas
# """
#
# df['date_month_weekly'] = df['date'].dt.strftime('%B-%d-%Y') #formato pakeitimas, B - tai menesio pavadinimas 3 raidem
# # print(df)
# df['date_month_weekly'] = df['date'].dt.strftime('%B/%d/%Y') #formato pakeitimas, B - tai menesio pavadinimas 3 raidem
# print(df)



# df = pd.DataFrame({
#     'A':[1, 2, 3, 4, 5, 1, 2, 3],
#     'B':['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']
# })
#
# unique_values_A = df['A'].unique()
# print('Unique values in A df A:',  unique_values_A)
# df_no_duplicates = df.drop_duplicates()
# print()
# df_no_duplicates_B = df.drop_duplicates(subset=['B'])
# print('DataFrame after removing duplicates:\n', df_no_duplicates_B)

# df1 = pd.DataFrame({
#     'EmployeeID': [1, 2, 3, 4, 5],
#     'Name': ['John', 'Smith', 'Cris', 'Jane', 'Bob']
# })
# df2 = pd.DataFrame({
#     'EmployeeID': [1, 2, 4, 5, 6],
#     'Department': ['HR', 'IT', 'Marketing', 'Finance', 'Engineering']
# })
#
# merged_df = pd.merge(df1, df2, on='EmployeeID', how='outer') #how='outer', tada rodo ir tuos, kurie neatitiko, rodo "NaN", o be how='outer' - tada tik tiek kiek suranda atitikimu
# print(merged_df)

# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2', 'A3'],
#     'B': ['B0', 'B1', 'B2', 'B3']
# })
#
# df2 = pd.DataFrame({
#     'C': ['C0', 'C1', 'C2', 'C3'],
#     'D': ['D0', 'D1', 'D2', 'D3']
# })
#
# # joined_df = df1.join(df2)
# # print('joined df:\n', joined_df)
#
# concatenated_vertical = pd.concat([df1, df2], axis=1)
# print(concatenated_vertical)

# data = {
#     'Skyrius': ['IT', 'Vadyba', 'IT', 'Vadyba'],
#     'darbuotojas': ['Jonas', 'Ona', 'Petras', 'Ieva'],
#     'atlyginimas': [3000,3500,2800,3100],
#     'tipas': ['Tipas A', 'Tipas B','Tipas A', 'Tipas B']
#  }
# df = pd.DataFrame(data)
#
# rezultatas = df.groupby(['Skyrius', 'tipas'])['atlyginimas'].agg(['max', 'mean']).reset_index()
# print(rezultatas)
#
# DataFrame darbuotojai turi stulpelius darbuotojo_id, vardas, atlyginimas, skyrius. Raskite visus darbuotojus,
# kurių atlyginimas yra didesnis nei 2000 ir jie dirba IT skyriuje.
# Panaudokite sąlyginį filtravimą ir pateikite galutinį DataFrame su šiais darbuotojais.


# darbuotojai = pd.DataFrame({
#     'darbutojo_id': [11,2,3,4],
#     'vardas': ['Juozas', 'Antanas', 'Ona', 'Maryte'],
#     'atlyginimas': [1500, 1700, 4000, 5000],
#     'skyrius': ['IT', 'Vadyba', 'IT', 'Marketingas']
#
# })

#darbuotojai2000_IT = darbuotojai[(darbuotojai['atlyginimas'] <2000) & (darbuotojai['skyrius']!='IT')]

#print(darbuotojai2000_IT)


#=============================================================================================================

# Jūsų turimas DataFrame objektas darbuotojai apima stulpelius: darbuotojo_id, vardas, pavardė, atlyginimas.
#     Rūšiuokite darbuotojai DataFrame pagal atlyginimas stulpelį didėjimo tvarka.
#     Rūšiuokite darbuotojai DataFrame pagal pavardė stulpelį abėcėlės tvarka, o ties vienodomis pavardėmis – pagal vardas stulpelį.

darbuotojai = pd.DataFrame({
    'darbutojo_id': [11,2,3,4],
    'vardas': ['Juozas', 'Antanas', 'Ona', 'Maryte'],
    'pavarde':['Juozaitis', 'Antanaitis', 'Onaitiene','Marytaitiene'],
    'atlyginimas': [1500, 1700, 4000, 5000],
})

pagal_atlyginimus = darbuotojai.sort_values('atlyginimas', ascending=False)
pagal_vardus = darbuotojai.sort_values(['vardas', 'pavarde'], ascending=True)

print(pagal_vardus)