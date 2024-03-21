
from Lietuvosrytas import gauti_naujienas
import sqlite3 as sqlite3

def irasyti_naujienas_i_DB(naujienos, db_failas='naujienos.db'):
    connection = sqlite3.connect(db_failas)
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS naujienos (antraste text)""")

    for antraste in naujienos:
        cursor.execute("INSERT INTO naujienos(antraste) VALUES(?)", (antraste,))

    connection.commit()
    connection.close()

naujienos = gauti_naujienas('https://www.lrytas.lt')
irasyti_naujienas_i_DB(naujienos)