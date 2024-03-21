import sqlite3 as sqlite3
from Knygos_funkcija_grazina_sarasa import knygu_sarasas


def create_db():
    conn = sqlite3.connect('knygos.db')
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS knygos(
    id INTEGER PRIMARY KEY,
    pavadinimas text,
    autorius text,
    metai int)""")

    conn.commit()
    conn.close()


def prideti_knyga(knygos):
    conn = sqlite3.connect('knygos.db')
    c = conn.cursor()
    for knyga in knygos:
        c.execute('INSERT INTO knygos (pavadinimas, autorius, metai) '
                  'VALUES (?, ?, ?)', (knyga['pavadinimas'], knyga['autorius'], knyga['metai']))

    conn.commit()
    conn.close()

def gauti_visas_knygas():
    conn = sqlite3.connect('knygos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM knygos')
    knygos = c.fetchall()
    conn.close()
    return knygos

rezultatas = knygu_sarasas()
create_db()
prideti_knyga(rezultatas)