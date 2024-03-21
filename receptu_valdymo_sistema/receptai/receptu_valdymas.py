class Receptas:
    def __init__(self, pavadinimas, ruosimo_laikas):
        self.pavadinimas = pavadinimas
        self.ruosimo_laikas = ruosimo_laikas

class ReceptuValdymas:
    def __init__(self):
        self.receptai = []


    def prideti_recepta(self, receptas):
        self.receptai.append(receptas)


    def gauti_receptus_pagal_laika(self, maksimalus_laikas):
        return [receptas for receptas in self.receptai if receptas.ruosimo_laikas <= maksimalus_laikas]

