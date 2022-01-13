from strona import Strona

class AlgorytmWymianyStron:

    def wybierz_strone(self, dostepne_zadania) -> Strona :
        raise NotImplementedError("Błąd - nie zaimplementowano metody")

########################################################################

class AlgotyrmLFU(AlgorytmWymianyStron):

    def wybierz_strone(self, dostepne_zadania) -> Strona:
        pass
    
    def __str__(self) -> str:
        return "\nWyniki algorytmu LFU\n"

########################################################################

class AlgorytmMFU(AlgorytmWymianyStron):

    def wybierz_strone(self, dostepne_zadania) -> Strona:
        pass

    def __str__(self) -> str:
        return "\nWyniki algorytmu MFU\n"