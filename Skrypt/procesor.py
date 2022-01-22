from ramka import Ramka
from zadanie import Zadanie
from ustawienia import *
from statystyka import Statystyka
from algorytmy_szereg import AlgorytmSJF, AlgotyrmLCFS
from algorytmy_wymiany_stron import AlgorytmMFU, AlgotyrmLFU

class Procesor:

    def __init__(self, algorytm):

        self.lista_ciagow = []
        self.algorytm=algorytm
        self.statystyka_ogolna = Statystyka()

    ########################################################################

    def uszereguj_ciagi_zad (self):
        print (self.algorytm)
        self.wczytaj_zad()

        for ciag in self.lista_ciagow:
            self.szereguj_zad(ciag)

        print("\nOgólne statystyki: (czas spóźnienia, czas cyklu)\n")
        print(self.statystyka_ogolna)

    ########################################################################

    def uszereguj_ciagi_stron (self):
        print (self.algorytm)
        self.wczytaj_strony()

        for ciag in self.lista_ciagow:
            self.szereguj_strony(ciag)

        print("\nOgólne statystyki: (ilość zmian stron)\n")
        print(self.statystyka_ogolna.srednia_ilosc_podmian_stron())

    ########################################################################

    def szereguj_zad (self, ciag: list):

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

                zadanie_wykonywane = self.algorytm.wybierz_zadanie(zadania_przygotowane)
                zadania_przygotowane.remove(zadanie_wykonywane)

                statystyka_ciagu.czas_spoznienia.append(t - int(zadanie_wykonywane.t_nad))
                t += int(zadanie_wykonywane.t_wyk)
                statystyka_ciagu.czas_cyklu.append(t - int(zadanie_wykonywane.t_nad))

        print(statystyka_ciagu)
        self.statystyka_ogolna.czas_spoznienia.append(statystyka_ciagu.sredni_czas_spoznienia())
        self.statystyka_ogolna.czas_cyklu.append(statystyka_ciagu.sredni_czas_cyklu())

    ########################################################################

    def szereguj_strony (self, ciag: list):
        self.algorytm.resetuj_ilosc_wystapien()
        licznik_podmian = 0
        ramka = Ramka(ROZMIAR_RAMKI)

        for strona in ciag:
            if ramka.czy_zawiera(strona):
                pass
            else: 
                licznik_podmian +=1
                numer_miejsca_w_ramce = self.algorytm.wybierz_miejsce_w_ramce(ramka,strona)
                ramka.zmien_strone(numer_miejsca_w_ramce, strona)
            
            self.algorytm.dodaj_wystapienie(strona)

        print(licznik_podmian)
        self.statystyka_ogolna.ilosc_podmian_stron.append(licznik_podmian)
    
    ########################################################################

    def wczytaj_zad (self):
        
        plik = open("lista_ciagow_zadan.txt", "r")
        
        for i in range(0, ILOSC_CIAGOW):
            ciag_zadan = []
            for j in range(0, ILOSC_ZADAN_W_CIAGU):
                nowe_zad = Zadanie()
                [nowe_zad.t_wyk, nowe_zad.t_nad] = plik.readline().split("\t")

                ciag_zadan.append(nowe_zad)
            self.lista_ciagow.append(ciag_zadan)
        
        plik.close()

    ########################################################################

    def wczytaj_strony (self):
        
        plik = open("lista_ciagow_stron.txt", "r")
        
        for i in range(0, ILOSC_CIAGOW):
            ciag_stron = []
            for j in range(0, ILOSC_STRON_W_CIAGU):
                numer_strony = int(plik.readline())

                ciag_stron.append(numer_strony)
            self.lista_ciagow.append(ciag_stron)
        
        plik.close()