
from datetime import datetime

class TransportoPriemone:
    def __init__(self, gamintojas, modelis, metai, svoris):
        self.gamintojas = gamintojas
        self.modelis = modelis
        self.metai = metai
        self.svoris = svoris

    def informacija(self):
        print(f'Gamintojas:{self.gamintojas}')
        print(f'Modelis:{self.modelis}')
        print(f'Metai:{self.metai}')
        print(f'Svoris:{self.svoris}')

class Sunkvezimis(TransportoPriemone):
    def __init__(self, gamintojas, modelis, metai, svoris, krovinioTalpa, kuroSanaudos, nuvaziuotasAtstumas):
        super().__init__(gamintojas, modelis, metai, svoris)
        self.kroviniTalpa = krovinioTalpa
        self.kuroSanaudos = kuroSanaudos
        self.nuvaziuotasAtstumas = nuvaziuotasAtstumas


    def informacija(self):
        super().informacija()
        print(f'Krovinio talpa:{self.krovinioTalpa}')
        print(f'Kuro sanaudos:{self.kuroSanaudos}')
        print(f'Nuvaziuotas Atstumas:{self.nuvaziuotasAtstumas}')

    def nuvaziuotas_atstumas(self):
        return self.nuvaziuotasAtstumas >100000



class Mikroautobusas(TransportoPriemone):
    def __init__(self, gamintojas, modelis, metai, svoris, sedimuVietuSkaicius, prieziurosGrafikas):
        super().__init__(gamintojas, modelis, metai, svoris)
        self.sedimuVietuSkaicius = sedimuVietuSkaicius
        self.prieziurosGrafikas = prieziurosGrafikas

    def informacija(self):
        super().informacija()
        print(f'Sedimu vietu skaicius:{self.sedimuVietuSkaicius}')
        print(f'Prieziuros grafikas:{self.prieziurosGrafikas}')

    def reikia_technines_pprieziuros(self):
        return (datetime.datetime.now() - self.prieziurosGrafikas) days > 365




class ElektrinisPaspirtukas(TransportoPriemone):
    def __init__(self, gamintojas, modelis, metai, svoris, baterijosLygis, nuvaziuojamasAtstumas):
        super().__init__(gamintojas, modelis, metai, svoris)
        self.baterijosLygis = baterijosLygis
        self.nuvaziuojamasAtstumas = nuvaziuojamasAtstumas


    def informacija(self):
        super().informacija()
        print(f'Baterijos lygis:{self.baterijosLygis}')
        print(f'Nuvaziuojamas atstumas:{self.nuvaziuojamasAtstumas}')

    def bterijos_lygis(self):
        return self.baterijosLygis < 20

class TransportoParkoValdymas:
    def __init__(self):
        self.transporto_Priemones = []


    def prideti_transporto_priemone(self, transporto_priemone):
        self.transporto_Priemones.append(transporto_priemone):

    def rodyti_bendra_prieziuros_grafika(self):
       # return [tp for tp in self.transporto_Priemones if tp.reikia_technines_pprieziuros()]
    priemones_reikalaujancios_pprieziuros = []
    for tp in self.transporto_Priemones
        if tp.reikia_technines_pprieziuros():
            tp_informacija = {
                'gamintojas': tp.gamintojas,
                'modelis': tp.modelis,
                'metai': tp.metai,
                'svoris': f'{tp.svoris}kg'
            }
            if isinstance(tp, Sunkvezimis):
            tp_informacija ['krovinio talpa'] = f'{tp.krovinioTalpa} kg'
            tp_informacija [nuvaziuotas atstumas] = f'{tp.nuvaziuotasAtstumas} km'

            elif isinstance(tp, Mikroautobusas):
            tp_informacija ['Sedimu vietu skaicius'] = f'{tp.sedimuVietuSkaicius} vnt'
            tp_informacija ['Prieziuros graafikas'] = f'{tp.prieziurosgrafikas}'

        elif isinstance(tp, ElektrinisPaspirtukas):
            tp_informacija['baterijos lygis'] = f'{tp.baterijosLygis} %'
            tp_informacija['Prieziuros graafikas'] = f'{tp.prieziurosgrafikas}'
    def
        bendra_talpa = 0

        for tp in self.transporto_Priemones:
            if isinstance(tp, Sunkvezimis):
                bendra_talpa += tp.kroviniTalpa
        return bendra_talpa




priemones = TransportoPriemone
valdymas = TransportoPriemoniuValdymas
sunkvezimis1 = Sunkvezimis('MAN', 'G30', 2010, 4, 10, 20,5000)
sunkvezimis2 = Sunkvezimis('Volvo','X120',2015,6,10,25,9000)

mikroAutobusas1 = Mikroautobusas('daf','LT60',2000,1,12,'Testas')

elelktrinisPaspirtukas1 = ElektrinisPaspirtukas('CUBE', 'CB20',2010,30,18,40)
#valdymas.prideti_sunkvezimi(sunkvezimis1)
#valdymas.prideti_sunkvezimi(sunkvezimis2)

