import pytest
import sqlite3
import os
from Knygos_managerdb import prideti_knyga

@pytest.fixture
def test_db():
    db_failas = 'test_knygos.db'
    yield db_failas
    if os.path.exists(db_failas):
        os.remove(db_failas)

def test_prideti_knyga(test_db):
    knygos = [
        {

        }
    ]
    irasyti_naujienas_i_