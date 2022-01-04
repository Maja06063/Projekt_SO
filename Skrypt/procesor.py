from typing import List
from zadanie import Zadanie
from ustawienia import *
from statystyka import Statystyka
from algorytmy_szereg import AlgorytmSJF, AlgotyrmLCFS

class Procesor:

    statystyka_ogolna = Statystyka()
    list_ciag_zad = []
    algorytm_szeregowania = None

    ########################################################################

    def uszereguj_ciagi_zad (self):
        
        self.wczytaj_zad()

        for ciag in self.list_ciag_zad:
            self.szereguj_zad(ciag)

        print("\nOgólne statystyki:\n")
        print(self.statystyka_ogolna)

    ########################################################################

    def __init__(self, SJF):
        
        if SJF:
            self.algorytm_szeregowania = AlgorytmSJF()
        else:
            self.algorytm_szeregowania = AlgotyrmLCFS()

    ########################################################################

    def szereguj_zad (self, ciag: List):

        zadania_przygotowane = []
        t = 0
        statystyka_ciagu = Statystyka()

        while len(ciag) > 0 or len(zadania_przygotowane) > 0:

            for zadanie in ciag:
                if int(zadanie.t_nad) <= t:

                    zadania_przygotowane.append(zadanie)
                    ciag.remove(zadanie)

            if len(zadania_przygotowane) < 1:
                t += 1

            else:

                zadanie_wykonywane = self.algorytm_szeregowania.wybierz_zadanie(zadania_przygotowane)
                zadania_przygotowane.remove(zadanie_wykonywane)

                statystyka_ciagu.czas_spoznienia.append(t - int(zadanie_wykonywane.t_nad))
                t += int(zadanie_wykonywane.t_wyk)
                statystyka_ciagu.czas_cyklu.append(t - int(zadanie_wykonywane.t_nad))

        print(statystyka_ciagu)
        self.statystyka_ogolna.czas_spoznienia.append(statystyka_ciagu.sredni_czas_spoznienia())
        self.statystyka_ogolna.czas_cyklu.append(statystyka_ciagu.sredni_czas_cyklu())
    
    ########################################################################

    def wczytaj_zad (self):
        
        plik = open("lista_ciagow.txt", "r")
        
        for i in range(0, ILOSC_CIAGOW):
            ciag_zadan = []
            for j in range(0, ILOSC_ZADAN_W_CIAGU):
                nowe_zad = Zadanie()
                [nowe_zad.t_wyk, nowe_zad.t_nad] = plik.readline().split("\t")

                ciag_zadan.append(nowe_zad)
            self.list_ciag_zad.append(ciag_zadan)            