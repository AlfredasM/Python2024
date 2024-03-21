import pytest
from receptu_valdymo_sistema.receptai.receptu_valdymas import Receptas, ReceptuValdymas

@pytest.fixture
def receptu_valdymas():
    valdymas = ReceptuValdymas()
    valdymas.prideti_recepta(Receptas('Cezario salotos', 15))
    valdymas.prideti_recepta(Receptas('Makaronai su suriu', 30))
    valdymas.prideti_recepta(Receptas('Karbonadas', 45))
    return valdymas

def test_gauti_receptus_pagal_laika(receptu_valdymas):
    rezultatas = receptu_valdymas.gauti_receptus_pagal_laika(30)
    pavadinimai = [receptas.pavadinimas for receptas in rezultatas]
    assert 'Cezario salotos' in pavadinimai
    assert 'Makaronai su suriu' in pavadinimai
    assert 'Karbonadas' not in pavadinimai
