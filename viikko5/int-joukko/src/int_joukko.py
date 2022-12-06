from copy import deepcopy

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin on oltava nollaa suurempi kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon on oltava nollaa suurempi kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
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
        return len(self.ljono)

    def to_int_list(self):
        return deepcopy(self.ljono)

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

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
