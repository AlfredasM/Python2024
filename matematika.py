# import pytest
#
# def sudetis(a, b):
#     return a + b
#
#
# def daugyba(a, b):
#     return a * b

# def didziausias_skaicius(a, b):
#     return a if a > b else b
#
#
# def pasisveikinimas (vardas):
#     return f"Labas, {vardas}"
#
# def pirmas_elementas(sarasas):
#     return sarasas[0]
#
# def teksto_apvertimas(tekstas):
#     apverstas = tekstas[::-1]
#     return apverstas

# def skaiciu_suma(skaiciai):
#     return sum(skaiciai)

def filtruoti_teigiamus(sk_sarasas):
    return [x for x in sk_sarasas if x > 0]

# def gauti_prima_elementa(sarasas):
#     return sarasas[0] if sarasas else None


# def ar_dalus_3(skaicius):
#     return ( True if skaicius  % 3 == 0 else False)

# def rasti_pasikartojancius_zodzius(sarasas):
#     rezultatas = [zodis for zodis in sarasas if len(zodis) != len(set(zodis))]
#     return rezultatas

# def skaiciuotuvas(operacija, x, y):
#     if operacija == 'sudetis':
#         return x+y
#     elif operacija=='atimtis':
#         return x-y
#     elif operacija=='daugyba':
#         return x*y
#     elif operacija=='dalyba':
#        return x/y

import requests


# def gauti_http_status(url):
#     try:
#         response = requests.get(url)
#         return response.status_code
#     except requests.RequestException:
#         return None

# def vartotojo_amziaus_patikrinimas(amzius):
#     return amzius >= 18

# def skaiciu_filtravimas(sk_sarasas):
#     return [x for x in sk_sarasas if x > 3]


