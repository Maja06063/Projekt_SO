from zadanie import Zadanie

"""
Klasa AlgorytmSzereg jest klasą bazową obu wybranych algorytmów szeregowania zadań.
"""

class AlgorytmSzereg:

    def wybierz_zadanie(self, dostepne_zadania) -> Zadanie:
        raise NotImplementedError("Błąd - nie zaimplementowano metody")

########################################################################

"""
Klasa AlgotyrmLCFS implementuje użycie algorytmu szeregowania zadań Last came, first serviced.
"""

class AlgotyrmLCFS(AlgorytmSzereg):

    """
    Metoda wybierz_zadanie służy do wybrania zadania, które ma zostać wykonane w danej chwili czasu.

    Argumenty:
    dostepne_zadania - lista zadań, które już są dostępne - upłynął ich czas nadejścia.

    Zwraca:
    Ostatnie zadanie w kolejności nadania, które jest dostępne.
    """

    def wybierz_zadanie(self, dostepne_zadania) -> Zadanie:
        
        dostepne_zadania.sort(key=lambda zadanie: zadanie.t_nad)
        return dostepne_zadania[-1]

    def __str__(self) -> str:
        return "\nWyniki algorytmu LCFS\n"

########################################################################

"""
Klasa AlgotyrmSJF implementuje użycie algorytmu szeregowania zadań Shortest job first.
"""

class AlgorytmSJF(AlgorytmSzereg):

    """
    Metoda wybierz_zadanie służy do wybrania zadania, które ma zostać wykonane w danej chwili czasu.

    Argumenty:
    dostepne_zadania - lista zadań, które już są dostępne - upłynął ich czas nadejścia.

    Zwraca:
    Zadanie z najkrótszym czasem wykonywania, które jest dostępne.
    """

    def wybierz_zadanie(self, dostepne_zadania) -> Zadanie:
        
        dostepne_zadania.sort(key=lambda zadanie: zadanie.t_wyk)
        return dostepne_zadania[0]

    def __str__(self) -> str:
        return "\nWyniki algorytmu SJF\n"