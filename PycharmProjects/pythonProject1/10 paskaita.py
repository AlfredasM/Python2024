
#polimorfiskumas
#overriting
# class Gyvunas:
#
#     def garsas(self):
#         print("Garsas")
#
#
# class Kate(Gyvunas):
#     def garsas(self):
#         return "Kate miauksi.."


# class Suo(Gyvunas):
#     def garsas(self):
#         return "Suniukas loja.."
#
#
# def leisti_garsa(gyvunas):
#     print(gyvunas.garsas())
#
#
# kate = Kate()
# suo = Suo()
#
# leisti_garsa(kate)
# leisti_garsa(suo)
#
# #overloaading
# def pasisveikinimas(vardas, amzius=None):
#     if amzius is None:
#         return f"Labas, {vardas}"
#     else:
#         return f"Labas, {vardas}, tau yra {amzius} metu"
#
#
# print(pasisveikinimas('Jonas'))
# print(pasisveikinimas('Jonas', 30))



# class TransportoPriemone:
#     def vaziuoti(self):
#         print("Si transporto priemone nevaziuoja!")
#
#
# class Automobilis(TransportoPriemone):
#     def vaziuoti(self):
#         return 'Automobilis vaziuoja!'
#
#
# class Dviratis(TransportoPriemone):
#
#     def vaziuoti(self):
#         return 'Dviratis vaziuoja'
#
#
# def transportas_vaziuoja(transporto_priemone):
#     print(transporto_priemone.vaziuoti())
#
#
# transportas_vaziuoja(Automobilis())
# transportas_vaziuoja(Dviratis())

# class Sudetis:
#     def skaiciuoti(self, a, b):
#         return a + b
#
#
# class Atimtis:
#
#     def skaiciuoti(self, a, b):
#         return a - b
#
#
# class Dalyba:
#     def skaiciuoti(self, a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "Dalyba is nulio negalima!"
#
#
# def atlikti_skaiciavima(operacija, a, b):
#     print(operacija.skaiciuoti(a, b))
#
#
# atlikti_skaiciavima(Sudetis(), 10, 5)
# atlikti_skaiciavima(Atimtis(), 10, 5)
# atlikti_skaiciavima(Dalyba(), 10, 5)
# atlikti_skaiciavima(Dalyba(), 10, 0)

# class Pranesimas:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas
#
#     def siusti(self):
#         raise NotImplementedError("Si funkcija turi buti igyventinta isvestineje klaseje!")
#
# class ElPastas(Pranesimas):
#     def __init__(self, tekstas, adresas):
#         super().__init__(self, tekstas, adresas)
#         self.adresas = adresas
#
#     def siusti(self):
#         return f'Siunciamas laiskas i {self.adresas} su tekstu {self.tekstas}'
#
#
# class SMS(Pranesimas):
#     def __init__(self, tekstas, numeris):
#         super().__init__(self, tekstas, numeris)
#         self.numeris = numeris
#
#     def siusti(self):
#         return f'Siunciamas SMS i {self.numeris} su tekstu {self.tekstas}'
#
#
# class Facebook(Pranesimas):
#     def __init__(self, tekstas, vartotojo_vardas):
#         super().__init__(self, tekstas, vartotojo_vardas)
#         self.vartotojo_vardas = vartotojo_vardas
#
#     def siusti(self):
#         return f'Siunciamas pranesimas: {self.tekstas} issiustas vartotojui {self.vartotojo_vardas}'
#
# def siusti_pranesima(pranesimas):
#     print(pranesimas.siusti)
#
#
# email =ElPastas("Labas kaip laikais", 'test@test.lt')
# sms = SMS("Priminimas apie susitikima", '+3706526585')
# facebook = Facebook("Puikus profilis", 'Testuser01')
#
# siusti_pranesima(email)
# siusti_pranesima(sms)
# siusti_pranesima(facebook)

class Pranesimas:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def siusti(self):
        raise NotImplementedError("Si funkcija  turi buti igvendinta isvestineje klaseje!")


class ElPastas(Pranesimas):
    def __init__(self, tekstas, adresas):
        super().__init__(tekstas)
        self.adresas = adresas

    def siusti(self):
        return f'Siunciamas laiskas i {self.adresas} su tekstu {self.tekstas}'


class SMS(Pranesimas):
    def __init__(self, tekstas, numeris):
        super().__init__(tekstas)
        self.numeris = numeris

    def siusti(self):
        return f'Siunciama SMS i {self.numeris}: {self.tekstas}'


class Facebook(Pranesimas):
    def __init__(self, tekstas, vartotojo_vardas):
        super().__init__(tekstas)
        self.vartotojo_vardas = vartotojo_vardas

    def siusti(self):
        return f'Pranesimas: {self.tekstas} issiustas vartotojui {self.vartotojo_vardas}'


def siusti_pranesima(pranesimas):
    print(pranesimas.siusti())


email = ElPastas("Labas, kaip laikaisi?", 'example@pavyzdys.com')
sms = SMS("Priminimas apie susitikima!", '86000000003')
facebook = Facebook("Puikus tavo profilis!", 'TestUser00')
siusti_pranesima(email)
siusti_pranesima(sms)
siusti_pranesima(facebook)

