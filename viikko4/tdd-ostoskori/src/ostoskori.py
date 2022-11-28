from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._kori = {}
        self._tavaroita = 0
        self._hinta = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self._tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self._kori:
           self._kori[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self._kori[lisattava.nimi()] = Ostos(lisattava)
        self._tavaroita += 1
        self._hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        kori = []
        for ostos in self._kori:
            kori.append(self._kori[ostos])
        return kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
