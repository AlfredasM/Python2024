import pytest
import sqlite3
from db_manager import irasyti_naujienas_i_DB
import os

@pytest.fixture
def test_db():
    db_failas = 'test_naujienos.db'
    yield db_failas
    # Ištriname testinę DB po testo
    if os.path.exists(db_failas):
        os.remove(db_failas)


def test_irasyti_naujienas_i_db(test_db):
    naujienos = ['Test Naujiena 1', 'Test Naujiena 2']
    irasyti_naujienas_i_DB(naujienos, db_failas=test_db)

    # Patikriname, ar naujienos buvo įrašytos
    conn = sqlite3.connect(test_db)
    c = conn.cursor()
    c.execute("SELECT * FROM naujienos")
    gautos_naujienos = c.fetchall()

    # Užtikriname, kad gautų įrašų skaičius atitinka įrašytų naujienų skaičių
    assert len(gautos_naujienos) == len(naujienos)

    # Užtikriname, kad kiekviena naujiena yra teisinga
    for i, naujiena in enumerate(naujienos):
        assert gautos_naujienos[i][0] == naujiena

    c.close()
    conn.close()








