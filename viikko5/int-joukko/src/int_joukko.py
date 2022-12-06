from copy import deepcopy

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava nollaa suurempi kokonaisluku")
        else:
            self.ljono = [0] * kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon on oltava nollaa suurempi kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        else:
            return False

    def lisaa(self, n):
        if n not in self.ljono:
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.ljono):
                self.ljono = self.ljono + [0]*self.kasvatuskoko
            return True
        return False

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            if len(self.ljono) - self.alkioiden_lkm == self.kasvatuskoko:
                self.ljono = self.ljono[:-self.kasvatuskoko]
            return True
        return False

    def alkioiden_lukumaara(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return deepcopy(self.ljono[:self.alkioiden_lkm])

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for numero in a_taulu:
            yhdiste.lisaa(numero)

        for numero in b_taulu:
            yhdiste.lisaa(numero)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for numero in a_taulu:
            if numero in b_taulu:
                leikkaus.lisaa(numero)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        tuotos = "{"
        for i in range(0, len(self.ljono)-1):
            tuotos = tuotos + str(self.ljono[i]) + ", "
        tuotos = tuotos + str(self.ljono[-1])+ "}"
        return tuotos
