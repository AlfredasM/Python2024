import pandas as pd


class DuomenuRinkinys:
    def __init__(self):
        self.duomenys = None

    def ikeltiDuomenis(self, kelias_iki_failo):
        try:
            self.duomeneys = pd.read_csv('duomenys.csv')
            print("Duomenys sekmingai ikelti!")
        except FileNotFoundError:
            print(f"Failas {kelias_iki_failo} nerastas!")

    def valytiDuomenis(self):
        """ Pasalina trukstmas reiksmes"""
        if self.duomenys is not None:
            self.duomenys.dropna(inplace=True)
            print("trukstamos reiksmes pasalintos")
        else:
            print("Nera ikeltu duomenu valymui!")

    def transformuotiDuomenis(self):
        """Standartizuoja skaitines reiskmes """
        pass


duomenu_rinkinys = DuomenuRinkinys()
duomenu_rinkinys.ikeltiDuomenis('kelias-iki-failo')
duomenu_rinkinys.valytiDuomenis()
duomenu_rinkinys.transformuotiDuomenis()