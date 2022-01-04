from ustawienia import ILOSC_CIAGOW, ILOSC_ZADAN_W_CIAGU
from zadanie import Zadanie
import random

class Generator:

    def zapisz_liste_ciag (self, list_ciag_zad):
        plik = open("lista_ciagow.txt", "w")
        for ciag in list_ciag_zad:
            for zadanie in ciag:
                plik.write(str(zadanie) + "\n")
        plik.close()

    def generuj_zad (self)-> Zadanie:
        zad = Zadanie ()
        zad.t_nad = random.randint(0,400)
        zad.t_wyk = random.randint(1,20)
        return zad

    def generuj (self):
        list_ciag_zad = []
        for i in range(0, ILOSC_CIAGOW):
            ciag_zadan = []
            for j in range(0, ILOSC_ZADAN_W_CIAGU):
                nowe_zad = self.generuj_zad ()
                ciag_zadan.append(nowe_zad)
            list_ciag_zad.append(ciag_zadan)
        self.zapisz_liste_ciag (list_ciag_zad)


