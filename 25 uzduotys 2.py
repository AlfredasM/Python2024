import sqlite3

conn = sqlite3.connect('mokykla.db')
c = conn.cursor()


# c.execute("""
# CREATE TABLE mokiniai(
#     id INTEGER PRIMARY KEY,
#      vardas TEXT,
#      pavarde TEXT,
#      klase TEXT)
#      """)
#
# names = [('1', 'Jonas', 'Jonaitis', '6c' ), ('2', 'Antanas','Antanaitis', '7b'), ('3', 'Migle','Miglaite', '5a' )]
# c.executemany('INSERT INTO mokiniai VALUES (?, ?, ?, ?)', names)
#
# c.execute('SELECT * FROM mokiniai')
#
# result = c.fetchall()
# for row in result:
#     print(row)
#
# conn.commit()
# conn.close()

# c.execute("""
#
# """)