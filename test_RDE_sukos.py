import os

import pytest
from RDE_sukos_manager import create_db, prideti_produkta, gauti_visus_produktus
from RDE_sukos import gauti_info
import requests_mock



@pytest.fixture(scope="module")

def db_setup():
    create_db()
    yield
    os.remove('produktai.db')

class TestProduktai:
    def test_prideti_ir_gauti_produktus(self, db_setup):
        testiniai_produktai = [{'pavadinimas': 'produktas1', 'kaina': '10,99', 'kiekis': 5}]

        prideti_produkta(testiniai_produktai)
        produktai_db = gauti_visus_produktus()
        assert any (p[1] == 'produktas1' for p in produktai_db)
        # assert (2, 'produktas2', '11,99', 3) in produktai_db

mock_html = '''
<!DOCTYPE html>
<html lang="en">
<body>
<li class='col col--xs-4 product js-product js-touch-hover'>
<h3 class='product__title'>produktas1</h3>
<p class = 'price'>10.99</p>
</li>
<li class='col col--xs-4 product js-product js-touch-hover'>
<h3 class='product__title'>produktas2</h3>
<p class = 'price'>11.99</p>
</li>
</body>
</html>
'''

def test_gauti_info():
    test_url = 'http://www.labadiena.lt/produktai'
    expected_response = [{'pavadinimas' : 'produktas1', 'kaina': '10.99', 'kiekis' : 1},
                         {'pavadinimas' : 'produktas2', 'kaina': '11.99', 'kiekis' : 1}]
    with requests_mock.Mocker() as m:
        m.get(test_url, text=mock_html)
        result = gauti_info(test_url)
    assert result == expected_response

