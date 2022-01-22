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
    Metoda nic nie zwraca
    """
    def __init__(self,rozmiar) -> None:
        self.rozmiar = rozmiar
        self.miejsce_w_ramce = [0]*rozmiar
    """
    Metoda zmien_strone  zawiera sposób opisu tekstowego obiektu Ramka.

    Argumenty:
    Metoda przyjmuje argumenty: numer_miejsca_w_ramce,strona.

    Zwraca:
    Metoda nic nie zwraca
    """
        

    def zmien_strone(self,numer_miejsca_w_ramce,strona):
        self.miejsce_w_ramce[numer_miejsca_w_ramce] = strona

"""
    Metoda init zawiera sposób opisu tekstowego obiektu Ramka.

    Argumenty:
    Metoda argument strona

    Zwraca:
    Metoda zwraca miejsce_w_ramce.
    """

    def czy_zawiera(self,strona) -> bool:
        return strona in self.miejsce_w_ramce