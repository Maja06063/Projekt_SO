from zadanie import Zadanie
from ustawienia import *
from statystyka import Statystyka
from algorytmy_szereg import AlgorytmSJF, AlgotyrmLCFS

class Procesor:

    statystyka = None
    list_ciag_zad = []
    algorytm_szeregowania = None

    def uszereguj_ciagi_zad (self):
        
        self.wczytaj_zad()

        for ciag in self.list_ciag_zad:
            self.szereguj_zad(ciag)

    def __init__(self):
        pass

    def szereguj_zad (self, ciag):
        pass
    
    def wczytaj_zad (self):
        
        plik = open("lista_ciagow.txt", "r")
        
        for i in range(0, ILOSC_CIAGOW):
            ciag_zadan = []
            for j in range(0, ILOSC_ZADAN_W_CIAGU):
                nowe_zad = Zadanie()
                [nowe_zad.t_wyk, nowe_zad.t_nad] = plik.readline().split("\t")
                print(nowe_zad)

                ciag_zadan.append(nowe_zad)
            self.list_ciag_zad.append(ciag_zadan)            