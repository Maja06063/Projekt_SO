"""
Klasa Zadanie zajmuje się przechowywaniem podstawowych informacji o danym zadaniu,
czyli czasie wykonania i czasie nadejścia.
"""

class Zadanie:

    t_wyk = 0
    t_nad = 0

    """
    Metoda __str__ zawiera sposób opisu tekstowego obiektu zadanie.

    Argumenty:
    Metoda nie przyjmuje argumentów.

    Zwraca:
    Tekst opisujący dany obiekt Zadanie.
    """

    def __str__(self) -> str:
        return str(self.t_wyk) + "\t" + str(self.t_nad)