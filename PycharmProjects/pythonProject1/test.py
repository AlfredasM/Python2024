def rasti_kompiuterius_pagal_kaina(self, maksimali_kaina):
    rasti_kompiuteriai = []
    for kompiuteris in self.inventorius:
        if kompiuteris.kaina < maksimali_kaina:
            rasti_kompiuteriai.append(kompiuteris)
    return rasti_kompiuteriai