# from matematika import sudetis, daugyba
#
# def test_sudetis():
#     num1, num2 = 2, 10
#     rezultatas = 15
#     faktinis_rezultatas = sudetis(num1, num2)
#     assert faktinis_rezultatas == rezultatas, (f"Sudeties testas nepavyko:{num1} + {num2}"
#                                                f" turetu buti {rezultatas}, bet gavome {faktinis_rezultatas}")
#
# def test_daugyba():
#     assert daugyba(2, 2) == 4
import pytest
from matematika import skaiciu_filtravimas


# from matematika import

# def test_didziausias_skaicius():
#     assert didziausias_skaicius(10, 5) == 10
#     assert didziausias_skaicius(2, 3) == 3
#     assert didziausias_skaicius(7, 7) == 7
#
# def test_pasisveikinimas():
#     assert pasisveikinimas('Tomas') == "Labas, Tomas"
#
#
# def test_pirmas_elementas():
#     assert pirmas_elementas([1, 2, 3, 4, 5]) == 1
#
# def test_teksto_apvertimas():
#     assert teksto_apvertimas('alus') == 'sula'

# def test_skaiciu_suma():
#     assert skaiciu_suma([5+10+15]) == 30

# def test_filtruoti_teigiamus():
#     assert filtruoti_teigiamus([-5, 10, 15, 1, 2, -10]) == [10, 15, 1, 2]
#     assert filtruoti_teigiamus([-1, -5, -10, -15]) == []

# @pytest.mark.parametrize("sarasas, tiketinas_rezultatas",[
#     ([1, 2, 3, 4, 5, 6], 1),
#     (['a', 'b', 'c', 'n'], 'a'),
#     ([], None),
#     ([[1, 2],[3, 4], [5, 6]], [1, 2])
#
# ])
#
# def test_gauti_pirma_elementa(sarasas, tiketinas_rezultatas):
#     assert gauti_prima_elementa(sarasas) == tiketinas_rezultatas


# @pytest.mark.parametrize("skaicius, rezultatas",[
#     ([6, True]),
#     ([9, True]),
#     ([100, False])
# ])
# def test_ar_dalus_3(skaicius, rezultatas):
#     assert ar_dalus_3(skaicius) == rezultatas

# @pytest.mark.parametrize("sarasas, sarasas_su_raidem",[
#     (['labas', 'namas', 'tvora'],['labas','namas']),
#      (['lyti', 'baltas', 'eiti'],['baltas', 'eiti']),
#       (['mama', 'alus', 'byra'],['mama'])
#
# ])
# def test_rasti_pasikartojancius_zodzius(sarasas, sarasas_su_raidem):
#     assert rasti_pasikartojancius_zodzius(sarasas) == sarasas_su_raidem
# @pytest.fixture
# def vartotoju_sarasas():
#     return [
#         {'vardas': 'Jonas', 'amzius': 30},
#         {'vardas': 'Petras', 'amzius': 25},
#         {'vardas': 'Migle', 'amzius': 43}
#     ]
# def test_kliento_amzius (vartotoju_sarasas):
#     for vartotojas in vartotoju_sarasas:
#         assert vartotojas['amzius'] >= 20

# @pytest.fixture
# def vartotoju_sarasas():
#     return [
#         {'vardas': 'Jonas', 'amzius': 25},
#         {'vardas': 'Petras', 'amzius': 18},
#         {'vardas': 'Migle', 'amzius': 18}
#     ]
# def test_vartotojo_amzius (vartotoju_sarasas):
#     for vartotojas in vartotoju_sarasas:
#         assert vartotojas['amzius'] >= 18

# @pytest.fixture
# def tekstu_sarasas():
#     return [
#         {'Labas'},
#         {'Diena'},
#         {'Lietus'}
#     ]
# def test_tekstu_sarasas(tekstu_sarasas):
#     for tekstas in tekstu_sarasas:
#         assert tekstas.startswith('L')

# @pytest.fixture
# def tik_lyginiai():
#     return [10, 16, 20, 31]
#
# def test_tik_lyginiai(tik_lyginiai):
#     for sk in tik_lyginiai:
#         assert sk % 2 == 0

# @pytest.fixture
# def du_tekstai(t1, t2):
#     return t1 + t2
#
# def test_du_tekstai():
#     assert 'Labas'

# @pytest.fixture(params=[
#     ('sudetis', 2, 3, 5),
#     ('atimtis', 4, 3, 1),
#     ('daugyba', 5, 10, 50),
#     ('dalyba', 20, 5, 4)])
#
# def matematika(request):
#     return request.param
#
# def test_skaiciuotuvas(matematika):
#     operacija, x, y, numatytas_rezultatas=matematika
#     assert skaiciuotuvas(operacija, x, y) == numatytas_rezultatas


# @pytest.fixture(params=[
#     ('http://www.google.com', 200),
#     ('http://www.neegzituojantisurl.lt', None),
#     ('https://www.github.com', 200),
#     ('http://www.tikrai_ne_tinklapis.com', None)
#
# ])
#
# def url_tiketinas_statusas(request):
#     return request.param
#
# def test_gauti_http_status(url_tiketinas_statusas):
#     url, tiketinas_statusas = url_tiketinas_statusas
#     assert gauti_http_status(url) == tiketinas_statusas

# @pytest.fixture(params=[16, 18, 20, 17])
#
# def vartotojo_amzius(request):
#     return request.param
#
# def test_vartotojo_amzius(vartotojo_amzius):
#     numatytas_rezultatas = vartotojo_amzius >= 18
#     assert vartotojo_amziaus_patikrinimas(vartotojo_amzius) == numatytas_rezultatas
#
#
#     print(numatytas_rezultatas)


# @pytest.fixture(params=(1, 2, 3, 4, 5, 6))
# def skaiciai(request):
#     return request.param
#
#
# def test_skaiciu_filtravimas(skaiciai):
#     numatytas_rezultatas = skaiciai > 3
#     assert skaiciu_filtravimas(skaiciai) == numatytas_rezultatas
