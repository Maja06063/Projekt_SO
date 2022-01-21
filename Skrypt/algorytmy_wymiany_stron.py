from ustawienia import *

class AlgorytmWymianyStron:

    ilosc_wystapien = [0]*(LICZBA_STRON+1)

    def resetuj_ilosc_wystapien(self):
        for wystapienie in self.ilosc_wystapien:
            wystapienie = 0

    def wybierz_miejsce_w_ramce(self,ramka,numer_strony) -> int:
        raise NotImplementedError("Błąd - nie zaimplementowano metody")

    def dodaj_wystapienie(self,numer_strony):
        self.ilosc_wystapien [numer_strony] +=1

########################################################################

class AlgotyrmLFU(AlgorytmWymianyStron):

    def wybierz_miejsce_w_ramce(self,ramka,numer_strony) -> int:
        i_min = 0
        liczba_wystapien_min = 999

        for i in range(0,ramka.rozmiar): 
            if self.ilosc_wystapien [ramka.miejsce_w_ramce[i]] < liczba_wystapien_min:
                i_min = i
                liczba_wystapien_min = self.ilosc_wystapien [ramka.miejsce_w_ramce[i]]

        return i_min

    def __str__(self) -> str:
        return "\nWyniki algorytmu LFU\n"

########################################################################

class AlgorytmMFU(AlgorytmWymianyStron):

    def wybierz_miejsce_w_ramce(self,ramka,numer_strony) -> int:
        i_max = 0
        liczba_wystapien_max = 0

        for i in range(0,ramka.rozmiar): 
            if self.ilosc_wystapien [ramka.miejsce_w_ramce[i]] > liczba_wystapien_max:
                i_max = i
                liczba_wystapien_max = self.ilosc_wystapien [ramka.miejsce_w_ramce[i]]

        return i_max

    def __str__(self) -> str:
        return "\nWyniki algorytmu MFU\n"