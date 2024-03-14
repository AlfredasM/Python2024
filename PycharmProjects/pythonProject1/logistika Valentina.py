from datetime import datetime

class TransportoPriemone:
    def __init__(self, gamintojas, modelis, metai, svoris):
        self.gamintojas = gamintojas
        self.modelis = modelis
        self.metai = metai
        self.svoris = svoris


    def info(self):
        print(f'Transporto priemones gamintojas {self.gamintojas}')
        print(f'Transporto priemones modelis {self.modelis}')
        print(f'Transporto priemones pagaminimo metai {self.metai}')
        print(f'Transporto priemones svoris {self.svoris}')


class Sunkvezimis(TransportoPriemone):
    def __init__(self, gamintojas, modelis, metai, svoris, krovinioTalpa, kuroSanaudos, nuvaziuotiKm):
        super().__init__(gamintojas, modelis, metai, svoris)
        self.krovinioTalpa = krovinioTalpa
        self.kuroSanaudos = kuroSanaudos
        self.nuvaziuotiKm = nuvaziuotiKm
        print(f'Transporto priemones krovinio talpa {self.krovinioTalpa}')
        print(f'Transporto priemones kuro sanaudos {self.kuroSanaudos}')
        print(f'Transporto priemones nuvaziuoti km {self.nuvaziuotiKm}')

    # def prieziuros_grafikas(self, techninesPrieziurosData):
    #      for tikrinimo_data in self.techninesPrieziurosData:
    #          if tikrinimo_data == self.techninesPrieziurosData / 100000:
    #     self.prieziuros_grafikas.append(techninesPrieziurosData)

    def reikia_technines_prieziuros(self):
        return self.nuvaziuotiKm >100000


class Mikroautobusas(TransportoPriemone):
    def __init__(self, gamintojas, modelis, metai, svoris, sedimuVietuSkaicius, prieziurosGrafikas):
        super().__init__(gamintojas, modelis, metai, svoris)
        self.sedimuVietuSkaicius = sedimuVietuSkaicius
        self.prieziurosGrafikas = prieziurosGrafikas
        print(f'Transporto priemones sedimu vietu skaicius {self.sedimuVietuSkaicius}')
        print(f'Transporto priemones prieziuros grafikas {self.prieziurosGrafikas}')

    def reikia_technines_prieziuros(self):
        return (datetime.datetime.now() - self.prieziurosGrafikas).days > 365




class ElektrinisPaspirtukas(TransportoPriemone):
    def __init__(self, gamintojas, modelis, metai, svoris, baterijosLygis, nuvaziuojamasAtstumas):
        super().__init__(gamintojas, modelis, metai, svoris)
        self.baterijosLygis = baterijosLygis
        self.nuvaziuojamasAtstumas = nuvaziuojamasAtstumas
        print(f'Transporto priemones baterijos lygis {self.baterijosLygis}')
        print(f'Transporto priemones nuvaziuojamas atstumas {self.nuvaziuojamasAtstumas}')

    def reikia_technines_prieziuros(self):
        self.baterijosLygis < 20


class TransportoParkoValdymas:
    def __init__(self):
        self.transporto_priemones = []

    def prideti_transporto_priemone(self, transporto_priemone):
        self.transporto_priemones.append(transporto_priemone)

    def rodyti_bendra_prieziuros_grafika(self):
        # return [tp for tp in self.transporto_priemones if tp.reikia_technines_prieziuros()]
        priemones_reikalaujancios_prieziuros = []

        for tp in self.transporto_priemones:
            if tp.reikia_technines_prieziuros():
                tp_informacija = {
                    "gamintojas": tp.gamintojas,
                    "modelis": tp.modelis,
                    "metai": tp.metai,
                    "svoris": f'{tp.svoris} kg'
                }
                if isinstance(tp, Sunkvezimis):
                    tp_informacija['krovinioTalpa'] = f'{tp.krovinioTalpa}, kg'
                    tp_informacija['nuvaziuotoKm'] = f'{tp.nuvaziuotiKm} km'
                elif isinstance(tp, Mikroautobusas):
                    tp_informacija['sedimuVietuSkaicius'] = f'{tp.sedimuVietuSkaicius}, vnt'
                    tp_informacija['prieziurosGrafikas'] = f'{tp.prieziurosGrafikas} '
                elif isinstance(tp, ElektrinisPaspirtukas):
                    tp_informacija['baterijosLygis'] = f'{tp.baterijosLygis}, %'
                    tp_informacija['nuvaziuojamasAtstumas'] = f'{tp.nuvaziuojamasAtstumas}, km '

                priemones_reikalaujancios_prieziuros.append(tp_informacija)
        return priemones_reikalaujancios_prieziuros


    def visu_sunkvezimiu_talpa(self):
        bendra_talpa = 0

        for tp in self.transporto_priemones:
            if isinstance(tp, Sunkvezimis):
                bendra_talpa += tp.krovinioTalpa
        return bendra_talpa

valdymas = TransportoParkoValdymas()
valdymas.prideti_transporto_priemone(Sunkvezimis("Volv", "FH", 2018, 8000, 20000, 10, 120))
valdymas.prideti_transporto_priemone(Mikroautobusas("Mersedes", "Sprinter", 2019, 3000,  12, "2023-01-01"))
valdymas.prideti_transporto_priemone(ElektrinisPaspirtukas("Xiaomi", "M365", 2019, 12, 75, 30))

print(f"Bendra sunkvezimiu krovinio talpa: {valdymas.visu_sunkvezimiu_talpa()}")