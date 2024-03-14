from datetime import datetime


class Knyga:
    def __init__(self, ISBN, pavadinimas, autorius, metai):
        self.ISBN = ISBN
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai
        self.arSkolinama = False

    def __str__(self):
        return f"{self.pavadinimas} by {self.autorius} ({self.metai})"


class Skaitytojas:
    def __init__(self, skaitytojo_id, vardas, pavarde):
        self.skaitytojo_id = skaitytojo_id
        self.vardas = vardas
        self.pavarde = pavarde
        self.skolinamos_knygos = []

    def isduoti_knyga(self, knyga):
        if len(self.skolinamos_knygos) >= 3:
            print("Negalima skolintis daugiau nei 3 knygas.")
            return False
        if knyga.arSkolinama:
            print("Knyga jau išduota.")
            return False
        knyga.arSkolinama = True
        if not self._check_some_other_condition(knyga):
            print("Dėl tam tikrų priežasčių ši knyga negali būti išduota.")
            knyga.arSkolinama = False
            return False
        self.skolinamos_knygos.append(knyga)
        print(f"{knyga} išduodama {self.vardas} {self.pavarde}.")
        return True

    def _check_some_other_condition(self, knyga):
        return True

    def grazinti_knyga(self, knyga):
        if knyga in self.skolinamos_knygos:
            knyga.arSkolinama = False
            self.skolinamos_knygos.remove(knyga)
            print(f"{knyga} grąžinta.")

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"


class isdavimas:
    def __init__(self, knyga, skaitytojas):
        self.knyga = knyga
        self.skaitytojas = skaitytojas
        self.skolinimo_data = datetime.now().strftime("%Y-%m-%d")
        self.grazinimo_data = None

    def grazinti(self):
        self.grazinimo_data = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"Išdavimas: {self.knyga}, Skaitytojas: {self.skaitytojas}, išdavimo data: {self.skolinimo_data}, Grąžinimo data: {self.grazinimo_data or 'Negrąžinta'}"



knyga1 = Knyga("978-3-16-148410-0", "Haris Poteris ir Išminties Akmuo", "J.K. Rowling", 1997)
skaitytojas1 = Skaitytojas(1, "Jonas", "Jonaitis")

if skaitytojas1.isduoti_knyga(knyga1):
    skolinimas1 = isdavimas(knyga1, skaitytojas1)
    print(skolinimas1)
else:
    print("Knyga negali būti išduota.")

skaitytojas1.grazinti_knyga(knyga1)