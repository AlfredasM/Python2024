# abstrakti klase
#
# from abc import ABC, abstractmethod
#
#
# # class Gyvunas(ABC):
# #     @abstractmethod
# #     def garsas(self):
# #        pass
# #
# #
# # class Suo(Gyvunas):
# #
# #     def garsas(self):
# #         return "Suniukas loja"
# #
# #
# # class Kate(Gyvunas):
# #
# #     def garsas(self):
# #         return "Kate miauksi"
# #
# #
# # def leisti_garsa(gyvunas):
# #     print(gyvunas.garsas())
# #
# #
# # leisti_garsa(Suo())
# # leisti_garsa(Kate())
#
# # class Saskaita(ABC):
# #     def __init__(self, savininkas, balansas=0):
# #         self.savininkas = savininkas
# #         self.balansas = balansas
# #
# #     @abstractmethod
# #     def inesti(self, suma):
# #         pass
# #
# #     @abstractmethod
# #     def isimti(self, suma):
# #         pass
# #
# #     def gauti_balansa(self):
# #         return self.balansas
# #
# #     @abstractmethod
# #     def pinigu_pervedimas(self):
# #         pass
# #
# #
# # class TaupomojiSaskaita(Saskaita):
# #
# #     def inesti(self, suma):
# #         self.balansas += suma
# #         print(f"Inesta {suma} Eur. Naujas balansas: {self.balansas} Eur")
# #
# #     def isimti(self, suma):
# #         if suma <= self.balansas:
# #             self.balansas -= suma
# #             print(f"Isimta {suma}Eur. Naujas balansas: {self.balansas}Eur")
# #         else:
# #             print("Nepakankamas balansas!")
# #
# #     def pinigu_pervedimas(self, kita_saskaita, suma):
# #         if self.balansas >=suma:
# #             self.balansas -= suma
# #             kita_saskaita.balansas +=suma
# #             print(f"Suma i {suma} sekmingai pervesta!")
# #         else:
# #             print("Nepakankamas balansas!")
# #
# #
# # class PapildomaSaskaita(Saskaita):
# #     def __init__(self, savininkas, balansas=0, dienos_limitas=500):
# #         super().__init__(savininkas, balansas)
# #         self.dienos_limitas = dienos_limitas
# #         self.isimta_siandien = 0
# #
# #     def inesti(self, suma):
# #         self.balansas += suma
# #         print(f"Inesta {suma} Eur. Naujas Balansas: {self.balansas}EUR")
# #
# #     def isimti(self, suma):
# #         if suma + self.isimta_siandien > self.dienos_limitas:
# #             print(f"Virsijamas dienos isemimo limitas:{self.dienos_limitas}. Jau isimta {self.isimta_siandien} Eur ")
# #         elif suma <= self.balansas:
# #             self.balansas -= suma
# #             self.isimta_siandien += suma
# #             print(f"Isimta {suma} Eur! Naujas Balansas: {self.balansas}EUR"
# #                   f"Jau isimta siandien:{self.isimta_siandien} Eur")
# #         else:
# #             print("Nepakankamas balansas")
# #
# #
# #     def atnaujinti_dienos_suma(self):
# #         self.isimta_siandien = 0
# #         print("Dienos  isemimo limitas atnaujintas")
# #
# #     def pinigu_pervedimas(self, kita_saskaita, suma):
# #         if self.balansas >=suma:
# #             self.balansas -= suma
# #             kita_saskaita.balansas +=suma
# #             print(f"Suma i {suma} sekmingai pervesta!")
# #         else:
# #             print("Nepakankamas balansas!")
# #
# #
# #
# #
# #
# # taupomoji = TaupomojiSaskaita('Jonas', 1000)
# # # taupomoji.inesti(50)
# # # taupomoji.isimti(150)
# #
# # papildoma_saskaita = PapildomaSaskaita('Petras', 1000, 300)
# # # papildoma_saskaita.inesti(200)
# # papildoma_saskaita.isimti(200)
# # papildoma_saskaita.isimti(200)
# #
# # taupomoji.pinigu_pervedimas(papildoma_saskaita, 100)
#
# from abc import ABC, abstractmethod
#
# # from abc import ABC, abstractmethod
# #
# #
# # class InventoriausValdymas(ABC):
# #     @abstractmethod
# #     def prideti(self, preke):
# #         pass
# #
# #     @abstractmethod
# #     def salinti(self, preke):
# #         pass
# #
# #     @abstractmethod
# #     def ieskoti(self, **kriterijai):
# #         pass
# #
# #
# # class Kompiuteris:
# #     def __init__(self, id, procesorius, ram, diskas, kaina):
# #         self.id = id
# #         self.procesorius = procesorius
# #         self.ram = ram
# #         self.diskas = diskas
# #         self.kaina = kaina
# #
# #     def __str__(self):
# #         return (f"ID: {self.id}, Procesorius: {self.procesorius}, RAM: {self.ram} GB, "
# #                 f"Diskas: {self.diskas}, Kaina: {self.kaina}")
# #
# #
# # class KompiuteriuParduotuve(InventoriausValdymas):
# #     def __init__(self):
# #         self.inventorius = []
# #
# #     def prideti(self, kompiuteris):
# #         self.inventorius.append(kompiuteris)
# #
# #     def salinti(self, id):
# #         for kompiuteris in self.inventorius:
# #             if kompiuteris.id != id:
# #                 self.inventorius.remove(kompiuteris)
# #
# #
# #
# #     def ieskoti(self, maksimali_kaina):
# #         rasti_kompiuteriai = []
# #         for kompiuteris in self.inventorius:
# #             if kompiuteris.kaina <= maksimali_kaina:
# #                 rasti_kompiuteriai.append(kompiuteris)
# #         return rasti_kompiuteriai
# #
# #
# # inventorius = KompiuteriuParduotuve()
# #
# # inventorius.prideti(Kompiuteris(1, "Intel i5", 8, "256GB SSD", 800))
# # inventorius.prideti(Kompiuteris(2, "AMD Ryzen 5", 16, "512GB SSD", 550))
# #
# # #inventorius.salinti(1)
# #
# # rezultatai = inventorius.ieskoti(600)
# # for kompiuteris in rezultatai:
# #     print(kompiuteris)
#
#
#
# # from abc import ABC, abstractmethod
# # from datetime import datetime, timedelta
# #
# # class Preke(ABC):
# #     def __init__(self, pavadinimas, kaina, id):
# #         self.pavadinimas = pavadinimas
# #         self.kaina = kaina
# #         self.id = id
# #
# #     @abstractmethod
# #     def informacija(self):
# #         print(f"Pavadinimas: {self.pavadinimas}, Kaina: {self.kaina}, ID: {self.id}")
# #
# # class Elektronika(Preke):
# #     def __init__(self, pavadinimas, kaina, id, garantija):
# #         super().__init__(pavadinimas, kaina, id)
# #
# #         if garantija <= 0:
# #             raise ValueError("Garantijos laikotarpis negali buti neigiamas")
# #         self.garantija = garantija
# #
# #     def informacija(self):
# #         print(f"Pavadinimas: {self.pavadinimas}, Kaina: {self.kaina} Eur, ID: {self.id}, Garantija: {self.garantija} men" )
# #
# #
# # class Maistas(Preke):
# #     def __init__(self, pavadinimas, kaina, id, galiojimo_data):
# #         super().__init__(pavadinimas, kaina, id)
# #         self.galiojimo_data = datetime.strptime(galiojimo_data, '%Y-%m-%d')
# #
# #     def informacija(self):
# #         if self.galiojimo_data >= datetime.now() :
# #             print(f"Pavadinimas: {self.pavadinimas}, Kaina: {self.kaina} Eur, ID: {self.id}, Galiojimo data : {self.galiojimo_data}")
# #         else:
# #             print("Produktas nebegalioja")
# #
# #
# # preke1 = Elektronika('Saldytuvas', 50, 2, 12 )
# # preke2 = Maistas('Duona', '20', 1, '2024-04-02')
# #
# # preke1.informacija()
# # preke2.informacija()
#
# from abc import ABC, abstractmethod
#
# from abc import ABC, abstractmethod

# class Preke(ABC):
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#
#     @abstractmethod
#     def panaudoti(self):
#         print(f"Panaudojama prekė: {self.pavadinimas}")
#
# class Zaislas(Preke):
#     def panaudoti(self):
#         super().panaudoti()
#         print(f'Zaislas: {self.pavadinimas}')
#         print("Žaislas naudojamas žaisti.")
#
#
# zaislas = Zaislas('Lele')
# zaislas.panaudoti()

# from abc import ABC, abstractmethod
#
# class Preke(ABC):
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#
#     @abstractmethod
#     def panaudoti(self):
#         pass
#
# class Zaislas(Preke):
#     def panaudoti(self):
#         print(f'Zaislas: {self.pavadinimas}')
#         print("Žaislas naudojamas žaisti.")
#
# zaislas = Zaislas('Lele')
# zaislas.panaudoti()
#
# from abc import ABC, abstractmethod
#
# class MokslinisDarbas(ABC):
#     @abstractmethod
#     def pateikti_santrauka(self):
#         pass
#
# class DiplominisDarbas(MokslinisDarbas):
#     def pateikti_santrauka(self):
#         print("Diplominio darbo santrauka.")
#
#
# from abc import ABC, abstractmethod
#
# from abc import ABC, abstractmethod
#
# class Prenumerata(ABC):
#     @abstractmethod
#     def gautiKaina(self):
#         pass
#
# class MetinePrenumerata(Prenumerata):
#     def __init__(self, kaina):
#         self.kaina = kaina
#
#
#
#     def gautiKaina(self):
#         print (f"Metine prenumeratos kaina: {self.kaina * 12}")
#
#
#
# met_prenumerata = MetinePrenumerata(20)
#
#
# met_prenumerata.gautiKaina()

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class VertinimoStrategijos(ABC):
    @abstractmethod
    def ivertinti(self):
        pass

class StrateginisZaidimas(VertinimoStrategijos):
    def ivertinti(self, zaidimas):
        print(f"Strateginis žaidimas '{zaidimas.pavadinimas}' įvertintas.")

class VeiksmoZaidimas(VertinimoStrategijos):
    def ivertinti(self,zaidimas):
        print(f"Veiksmo žaidimas '{zaidimas.pavadinimas}' įvertintas.")

class Zaidimas:
    def __init__(self, pavadinimas, zanras, vertinimo_strategija):
        self.pavadinimas = pavadinimas
        self.zanras = zanras
        self.vertinimo_strategija = vertinimo_strategija

    def ivertinti(self):
        self.vertinimo_strategija.ivertinti(self)



strateginis_zaidimas = Zaidimas('Strategija', 'strateginis', StrateginisZaidimas())
veiksmo_zaidimas = Zaidimas('Doom', 'veiksmo', VeiksmoZaidimas())
strateginis_zaidimas.ivertinti()
veiksmo_zaidimas.ivertinti()