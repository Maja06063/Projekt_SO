from ustawienia import *
from zadanie import Zadanie
import random

class Generator:

    def zapisz_liste_ciag (self, list_ciag_zad, nazwa_pliku):
        plik = open(nazwa_pliku, "w")
        for ciag in list_ciag_zad:
            for zadanie_lub_strona in ciag:
                plik.write(str(zadanie_lub_strona) + "\n")
        plik.close()

    ########################################################################

    def generuj_zad (self)-> Zadanie:
        zad = Zadanie ()
        zad.t_nad = random.randint(0,400)
        zad.t_wyk = random.randint(1,20)
        return zad

    ########################################################################
    def generuj_str (self)-> int:
        numer_strony=random.randint(1,LICZBA_STRON)
        return numer_strony

    ########################################################################

    def generuj (self,czy_strony):
        list_ciagow = []
        for i in range(0, ILOSC_CIAGOW):
            if czy_strony:
                ciag_stron = []
                for j in range(0, ILOSC_STRON_W_CIAGU):
                    nowe_zad = self.generuj_str ()
                    ciag_stron.append(nowe_zad)
                list_ciagow.append(ciag_stron)
            else:       
                ciag_zadan = []
                for j in range(0, ILOSC_ZADAN_W_CIAGU):
                    nowe_zad = self.generuj_zad ()
                    ciag_zadan.append(nowe_zad)
                list_ciagow.append(ciag_zadan)
        if czy_strony:
            self.zapisz_liste_ciag (list_ciagow,"lista_ciagow_stron.txt")
        else:
            self.zapisz_liste_ciag (list_ciagow,"lista_ciagow_zadan.txt")

    