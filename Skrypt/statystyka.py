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

    def sredni_czas_spoznienia(self) -> float:
        return sum(self.czas_spoznienia) / len(self.czas_spoznienia)

    def sredni_czas_cyklu(self) -> float:
        return sum(self.czas_cyklu) / len(self.czas_cyklu)

    def __str__(self) -> str:
        return str(self.sredni_czas_spoznienia()) + \
            ";"  + str(self.sredni_czas_cyklu())

    def srednia_ilosc_podmian_stron (self) -> float:
        return sum(self.ilosc_podmian_stron) / len(self.ilosc_podmian_stron)