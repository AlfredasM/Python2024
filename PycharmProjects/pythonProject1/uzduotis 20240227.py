class Studentas:
    def __init__(self, studento_id, vardas, pavarde):
        self.studento_id = studento_id
        self.vardas = vardas
        self.pavarde = pavarde
        self.registruoti_kursai = []


    def registruotis_kursui(self, kursas):
        if kursas not in self.registruoti_kursai:
            self.registruoti_kursai.append(kursas)
            kursas.prideti_studenta(self)


    def atsisakyti_kurso(self, kursas):
        if kursas in self.registruoti_kursai:
            self.registruoti_kursai.remove(kursas)
            kursas.pasalinti_studenda(self)

    def __str__(self):
        return self.vardas, self.pavarde

class Destytojas:
    def __init__(self, destytojo_id, vardas, pavarde):
        self.destytojo_id = destytojo_id
        self.vardas = vardas
        self.pavarde = pavarde
        self.destomi_kursai = []

    def prideti_kursa(self, kursas):
        if kursas not in self.destomi_kursai:
            self.destomi_kursai.append(kursas)
            kursas.keisti_destytoja(self)

    def pasalinti_kursa(self, kursas):
        if kursas in self.destomi_kursai:
            self.destomi_kursai.remove(kursas)
            kursas.keisti_destytoja(None)

    def __str__(self):
        return self.vardas, self.pavarde

class Kursas:
    def __init__(self, kursas_id, pavadinimas):
        self.kursas_id = kursas_id
        self.pavadinimas = pavadinimas
        self.destytojo_id = None
        self.registruoti_studentai = []

    def prideti_studenta(self, studentas):
        if studentas not in self.registruoti_studentai:
            self.registruoti_studentai.append(studentas)



        def pasalinti_studenda(self, studentas):
            if studentas in self.registruoti_studentai:
                self.registruoti_studentai.remove(studentas)



    def keisti_destytoja(self, destytojas):
        self.destytojas = destytojas


    def __str__(self):
        return self.pavadinimas

    @staticmethod
    def analizuot_kursu_populiarumas():
        if not kursai:
            return None, None
        kurso_studentu_skaicius = {kursas:len(kursas.registruoti_studentai) for kursas in kursai}
        populiariausias_kursas = max(kurso_studentu_skaicius, key=kurso_studentu_skaicius_skaicius.get)
        maziau_populiarus = min(kurso_studentu_skaicius, key=kurso_studentu_skaicius)
        return populiariausias_kursas, maziau_populiarus

def rasti_populiariausia_kursa(kursai):
    max_studentu = 0
    populiariausias_kursas = None
    for kursas in kursai:
        if len(kursas.registruoti_studentai) > max_studentu:
            max_studentu = len(kursas.registruoti_studentai)
            populiariausias_kursas = kursas
    return populiariausias_kursas

studentas1 = Studentas(11, 'Jonas','Jonaitis')
studentas2 = Studentas(12,'Petraitis','Petraitis')
studentas3 = Studentas(13,'Kestas','Kestaitis')


destytojas1 = Destytojas(21, 'Liudas', 'Liudaitis')
destytojas2 = Destytojas(22,'Zigmas','Zigmaitis')


kursas1 =Kursas(31,'Fizikos')
kursas2 =Kursas(32,'Chemijos')

kursas1.prideti_studenta(studentas1)
kursas2.prideti_studenta(studentas2)

destytojas1.prideti_kursa(kursas2)

studentas1.registruotis_kursui(kursas2)

populiariausias_kursas = rasti_populiariausia_kursa([kursas1, kursas2])
print(f"Populiariausias kursas: {populiariausias_kursas}, Studentu skaicius: {len(populiariausias_kursas.registruoti_studentai)}")

















