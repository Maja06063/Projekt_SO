from zadanie import Zadanie
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
        zawartosc_pliku = plik.readlines()

        for linia in zawartosc_pliku:
            zadanie_tmczs = Zadanie()
            [zadanie_tmczs.nr, zadanie_tmczs.t_wyk, zadanie_tmczs.t_nad] = linia.split("\t")
            