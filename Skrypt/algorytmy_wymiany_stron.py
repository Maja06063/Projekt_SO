from ustawienia import *

"""
Klasa AlgorytmWymianyStron jest klasą bazową obu wybranych algorytmów wymiany strony.
"""

class AlgorytmWymianyStron:

    ilosc_wystapien = [0]*(LICZBA_STRON+1)

    """
    Metoda resetuj_ilosc_wystapien ustawia na 0 każdy element listy mówiącej o ilości wystąpień.
    
    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Metoda nic nie zwraca.
    """

    def resetuj_ilosc_wystapien(self):
        for wystapienie in self.ilosc_wystapien:
            wystapienie = 0

    """
    Szablon metody wybierz_miejsce_w_ramce - do zaimplementowania w klasach dziedziczących.
    """

    def wybierz_miejsce_w_ramce(self,ramka,numer_strony) -> int:
        raise NotImplementedError("Błąd - nie zaimplementowano metody")

    """
    Metoda dodaj_wystapienie inkrementuje licznik wystąpień dla danego numeru strony.

    Argumenty:
    numer_strony - numer strony, której ilość wystąpień należy powiększyć.

    Zwraca:
    Metoda nic nie zwraca.
    """

    def dodaj_wystapienie(self,numer_strony):
        self.ilosc_wystapien [numer_strony] +=1

########################################################################

"""
Klasa AlgotyrmLFU implementuje użycie algorytmu wymiany strony Least frequently used.
"""

class AlgotyrmLFU(AlgorytmWymianyStron):

    """
    Metoda wybierz_miejsce_w_ramce służy do wybrania odpowiedniego miejsca w ramce
    dla danego numeru strony.

    Argumenty:
    ramka - Ramka wskazująca obecny stan stron wszytanych do pamięci,
    numer_strony - numer strony, dla której należy znaleźć odpowiednie miejsce w ramce.

    Zwraca:
    i_min - miejsce w ramce, do którego należy wstawić stronę o podanym numerze.
    """

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

"""
Klasa AlgotyrmMFU implementuje użycie algorytmu wymiany strony Most frequently used.
"""

class AlgorytmMFU(AlgorytmWymianyStron):

    """
    Metoda wybierz_miejsce_w_ramce służy do wybrania odpowiedniego miejsca w ramce
    dla danego numeru strony.

    Argumenty:
    ramka - Ramka wskazująca obecny stan stron wszytanych do pamięci,
    numer_strony - numer strony, dla której należy znaleźć odpowiednie miejsce w ramce.

    Zwraca:
    i_max - miejsce w ramce, do którego należy wstawić stronę o podanym numerze.
    """

    def wybierz_miejsce_w_ramce(self,ramka,numer_strony) -> int:

        # Uzupełnianie pustych stron w ramce:
        for i in range(0,ramka.rozmiar):
            if ramka.miejsce_w_ramce[i] == 0:
                return i

        # Poszukiwanie, którą stronę wymienić, gdy ramka jest pełna:
        i_max = 0
        liczba_wystapien_max = 0
        for i in range(0,ramka.rozmiar): 
            if self.ilosc_wystapien [ramka.miejsce_w_ramce[i]] > liczba_wystapien_max:
                i_max = i
                liczba_wystapien_max = self.ilosc_wystapien [ramka.miejsce_w_ramce[i]]

        return i_max

    def __str__(self) -> str:
        return "\nWyniki algorytmu MFU\n"