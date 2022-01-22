"""
Klasa Statystyka zajmuje się zapamiętywaniem wszelkich statystyk przebiegów symulacyjnych
dla różnych algorytmów. Zaznaczyć należy, że statystyka nie wie, dla jakiego algorytmu jest
prowadzona. Taką wiedzę posiada klasa procesor.
"""

class Statystyka:

    """
    Konstruktor klasy Statystyka.
    Wszelkie listy zostały zadeklarowane w konstruktorze, aby mieć pewność, że będą niezależne
    dla każdego utworzonego obiektu.
    """

    def __init__(self):
        self.czas_spoznienia = []
        self.czas_cyklu = [] 
        self.ilosc_podmian_stron = []

    ########################################################################

    """
    Metoda sredni_czas_spoznienia wylicza średnią z zapisanych czasów spóźnienia.

    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Średnią arytmetyczną czasu spóźnień.
    """

    def sredni_czas_spoznienia(self) -> float:
        return sum(self.czas_spoznienia) / len(self.czas_spoznienia)

    ########################################################################

    """
    Metoda sredni_czas_cyklu wylicza średnią z zapisanych czasów cyklu.

    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Średnią arytmetyczną czasu cykli.
    """

    def sredni_czas_cyklu(self) -> float:
        return sum(self.czas_cyklu) / len(self.czas_cyklu)

    ########################################################################

    """
    Metoda srednia_ilosc_podmian_stron wylicza średnią z ilości podmian stron. 

    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Średnią arytmetyczną z ilości podmian stron.
    """

    def srednia_ilosc_podmian_stron (self) -> float:
        return sum(self.ilosc_podmian_stron) / len(self.ilosc_podmian_stron)
 
    ########################################################################

    """
    Metoda __str__ zawiera sposób opisu tekstowego obiektu Statystyka.

    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Tekst opisujący dany obiekt Statystyka.
    """

    def __str__(self) -> str:
        return str(self.sredni_czas_spoznienia()) + \
            ";"  + str(self.sredni_czas_cyklu())