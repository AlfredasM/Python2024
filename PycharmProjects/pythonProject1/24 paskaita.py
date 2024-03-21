import sqlite3

conn = sqlite3.connect('test1.db')
c = conn.cursor()

# #sukurimas lenteles
# c.execute("""
# CREATE TABLE people(
#     id INTEGER PRIMARY KEY,
#      name TEXT,
#      age int)
#      """)
#
# names = [('1', 'Jonas', 34), ('2', 'Antanas', 35), ('3', 'Migle', 23)]
# c.executemany('INSERT INTO people VALUES (?, ?, ?)', names)
#
# c.execute('SELECT * FROM people')
#
# result = c.fetchall()
# for row in result:
#     print(row)
#
# conn.commit()
# conn.close()

#sukurimas lenteles
# c.execute("""
#     CREATE TABLE jobs (
#     id INTEGER PRIMARY KEY,
#      job_title text,
#      person_id INTEGER,
#      FOREIGN KEY (person_id) REFERENCES people(id))
#      """)
#
# jobs = [('1', 'Inzinierius', '1'), ('2', 'Programuotojas', '2'), ('3', 'Analitikas', '3')]
# c.executemany('INSERT INTO jobs VALUES (?, ?, ?)', jobs)

# c.execute(""" SELECT people.name, jobs.job_title from people
#             JOIN jobs on people.id = jobs.person_id
# """)
#
# result = c.fetchall()
# print(result)

# c.execute("""
#     CREATE TABLE hobbies (
#     id INTEGER PRIMARY KEY,
#     hobby text,
#     person_id INTEGER,
#     FOREIGN KEY (person_id) REFERENCES people(id))
# """)
# hobbies = [('1', 'Tennis', '1'), ('2', 'Voleybball', '2'), ('3', 'Cycling', '3')]
# aditional_hobbies = [('Sokti', '1'),
#                      ('Begti', '2') ]
#
# c.executemany('INSERT INTO hobbies(hobby, person_id) VALUES (?, ?)', aditional_hobbies)
# c.execute("""
#    SELECT people.name, hobbies.hobby from people
#    JOIN hobbies on people.id = hobbies.person_id
#    WHERE people.name = 'Jonas'
# """)
# result = c.fetchall()
# print(result)
# c.executemany('INSERT INTO hobbies VALUES (?, ?, ?)', hobbies)

# c.execute("""
#         INSERT INTO hobbies(hobby, person_id) VALUES('fishing', '1'), ('reading', '2'), ('programing', '3')
# """)

# c.execute("""
#     SELECT people.name, hobbies.hobby from people
#     JOIN hobbies on people.id = hobbies.id
# """)
# results = c.fetchall()
# print(results)

# c.execute("""
#     UPDATE hobbies SET hobby = 'Groti' WHERE person_id = (SELECT id from people WHERE name = 'Jonas')
#      and hobby = 'Tennis'
# """)

# c.execute("""
#     SELECT * FROM
#
#     (SELECT people.name as vardas, COUNT(hobbies.hobby) as hobiu_skaicius
#     FROM people
#     JOIN hobbies ON hobbies.person_id = people.id
#     GROUP BY people.id)
#
#     WHERE hobiu_skaicius > 1;
#     """)
# ans4 = c.fetchall()
# print(ans4)

c.execute(""" SELECT people.name, GROUP_CONCAT(hobbies.hobby) as hobbies_lis, COUNT(hobbies.hobby)
        as hobiu_bent_2 from hobbies
         JOIN people on people.id = hobbies.person_id
         GROUP BY people.id
         HAVING hobiu_bent_2 > 1
        """)
result = c.fetchall()
print(result)


# c.execute(""" SELECT people.name, hobbies.hobby from people
# join hobbies on people.id = hobbies.person_id
# order by people.name""")
# current_person = ''
# result = c.fetchall()
# for person_name, hobby in result:
#     if person_name != current_person:
#         print(f'{person_name} has the following hobbies:')
#         current_person = person_name
#     print(f'- {hobby}')





conn.commit()
conn.close()
