import sqlite3



# Sukurkite lentelę knygos su šiais stulpeliais:
#
# * id (sveikasis skaičius, pirminis raktas),
# * pavadinimas (tekstas),
# * autorius (tekstas),
# * isleidimo_metai (sveikasis skaičius),
# * puslapiu_skaicius (sveikasis skaičius).


conn = sqlite3.connect('test1.db')
c = conn.cursor()

# c.execute("""
#     CREATE TABLE knygos1(
#     id INTEGER PRIMARY KEY,
#     pavadinimas text,
#     autorius text,
#     isleidimo_metai INTEGER,
#     puslapiu_skaicius INTEGER)
# """)

# knygos1 = [('1', 'Knyga1', 'Autorius1', '2010', '500'),
#           ('2', 'Knyga2', 'Autorius2', '2005', '1500'),
#           ('3', 'Knyga3','Autorius3', '1995', '2500')]
# c.executemany('INSERT INTO knygos1 VALUES (?, ?, ?, ?, ?)', knygos1)

# c.execute('SELECT * FROM knygos1')
#
# result = c.fetchall()
# for row in result:
#     print(row)

# c.execute("""
#     SELECT knygos1.isleidimo_metai, knygos1.pavadinimas as nuo_2000 FROM knygos1
#     WHERE isleidimo_metai > 2000
#     ORDER BY isleidimo_metai DESC;
#
#
# """)
# result = c.fetchall()
# print(result)

# c.execute("""
#         UPDATE knygos1 SET puslapiu_skaicius = '5000' WHERE id = '3'
# """)

# c.execute("""
#     CREATE TABLE skaitytojai(
#     id INTEGER PRIMARY KEY,
#     vardas text,
#     pavarde text,
#     gimimo_metai INTEGER)
#
#     """)

# skaitytojai = [('1', 'Jonas', 'Jonaitis', '1975'),
#           ('2', 'Petras', 'Petraitis', '1985'),
#           ('3', 'Ona','Onaite', '1995')]
# c.executemany('INSERT INTO skaitytojai VALUES (?, ?, ?, ?)', skaitytojai)
#
# c.execute('SELECT * FROM skaitytojai')
#
# result = c.fetchall()
# for row in result:
#     print(row)

# c.execute("""
#     CREATE TABLE skaitytos_knygos (
#
#     skaitytojo_id INTEGER,
#     knygos_id INTEGER,
#     skaitymo_data DATE,
#     FOREIGN KEY (skaitytojo_id) REFERENCES skaitytojai(id),
#     FOREIGN KEY (knygos_id) REFERENCES knygos1(id))
#     """)
#
# skaitytos_knygos = [('1', '1', '2024-01-05'), ('2','2', '2024-02-05'), ('3','3', '2022-02-03')]
#
# c.executemany('INSERT INTO skaitytos_knygos VALUES (?, ?, ?)', skaitytos_knygos)
#
# c.execute('SELECT * FROM skaitytos_knygos')
#
# result = c.fetchall()
# for row in result:
#     print(row)

# c.execute("""
#     SELECT skaitytojai.vardas, skaitytojai.pavarde, knygos1.pavadinimas, skaitytos_knygos.skaitymo_data
#     FROM skaitytos_knygos
#     JOIN knygos1 ON  knygos1.id = skaitytos_knygos.knygos_id
#     JOIN skaitytojai ON skaitytojai.id = skaitytos_knygos.skaitytojo_id
#     GROUP BY knygos1.id
#  """)
# result = c.fetchall()
#
# print(result)






conn.commit()
conn.close()