class Klientas:
    def __init__(self, kliento_id, amzius, lytis):
        self.kliento_id = kliento_id
        self.amzius = amzius
        self.lytis = lytis
        self.pirkimo_istorija = []



    def prideti_pirkima(self, pirkimas):
        self.pirkimo_istorija.append(pirkimas)



    def gauti_pirkimo_istorija(self):
        return self.pirkimo_istorija



class Preke:
    def __init__(self, prekes_id, pavadinimas, kaina):
        self.prekes_id = prekes_id
        self.pavadinimas = pavadinimas
        self.kaina = kaina
        self.atsiliepimai = []



    def prideti_atsiliepima(self, reitingas):
        self.atsiliepimai.append(reitingas)




    def gauti_vidutini_reitinga(self):
        if not self.atsiliepimai:
            return None
        return sum(self.atsiliepimai) / len(self.atsiliepimai)



class Pirkimas:
    def __init__(self, pirkimo_id, kliento_id, prekes_id, kiekis):
        self.pirkimo_id = pirkimo_id
        self.kliento_id = kliento_id
        self.preles_id = prekes_id
        self.kiekis = kiekis


    def apskaiciuoti_suma(self, prekes_kaina):
        return self.kiekis * prekes_kaina




class AnalizesModulis:
    @staticmethod
    def rasti_populiariausia_preke(prekes):
        populiariausia = None
        auksciausias_reitingas = 0
        for preke in prekes:
            vidutinis_raitingas = preke.gauti_vidutini_reitinga()
            if vidutinis_raitingas is not None and vidutinis_raitingas > auksciausias_reitingas:
                populiariausia = preke
                auksciausias_reitingas = vidutinis_raitingas
        return populiariausia



klientas1 = Klientas(1, 28, 'M')
klientas2 = Klientas(2, 32, 'V')


preke1 = Preke(1043, 'Telefonas', 899.99)
preke2 = Preke(321, 'Nesiojamas kompiuteris', 1299.99)

preke1.prideti_atsiliepima(5)
preke1.prideti_atsiliepima(3)

preke2.prideti_atsiliepima(4)
preke2.prideti_atsiliepima(1)

pirkimas1 = Pirkimas(1,1,1043,1)
pirkimas2 = Pirkimas(2,2,321,1)

klientas1.prideti_pirkima(pirkimas1)
klientas2.prideti_pirkima(pirkimas2)


prekes = [preke1, preke2]

populiariausia_preke_pagal_reitinga = AnalizesModulis.rasti_populiariausia_preke(prekes)
if populiariausia_preke_pagal_reitinga:
    print(f"Populiariausia preke: {populiariausia_preke_pagal_reitinga.pavadinimas} su vidutiniu reitingu "
          f"{populiariausia_preke_pagal_reitinga.gauti_vidutini_reitinga()}")
else:
    print("Populiariausiu prekiu nerasta")