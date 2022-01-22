"""
Klasa Ramka odpowiedzialna jest za przechowywanie stron symulowanej pamięci.
"""

class Ramka:
    rozmiar = 0
    """
    Metoda init zawiera sposób opisu tekstowego obiektu Ramka.

    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Metoda nic nie zwraca.
    """
    def __init__(self,rozmiar) -> None:
        self.rozmiar = rozmiar
        self.miejsce_w_ramce = [0]*rozmiar
    
    ########################################################################

    """
    Metoda zmien_strone służy do zmiany numery strony na danym miejscu ramki.

    Argumenty:
    numer_miejsca_w_ramce - numer miejsca na którym zajdzie zmiana strony,
    strona - numer strony do wpisania w ramkę.

    Zwraca:
    Metoda nic nie zwraca
    """

    def zmien_strone(self,numer_miejsca_w_ramce,strona):
        self.miejsce_w_ramce[numer_miejsca_w_ramce] = strona

    ########################################################################

    """
    Metoda czy_zawiera sprawdza, czy dany numer strony już jest w ramce.

    Argumenty:
    Metoda argument strona - numer strony do sprawdzenia.

    Zwraca:
    Metoda zwraca prawda jeśli strona znajduje się w ramce,
    fałsz jeśli strona nie znajduje się w ramce.
    """

    def czy_zawiera(self,strona) -> bool:
        return strona in self.miejsce_w_ramce