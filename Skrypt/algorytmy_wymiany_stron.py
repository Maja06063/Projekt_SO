

class AlgorytmWymianyStron:

    def wybierz_strone(self) -> int:
        raise NotImplementedError("Błąd - nie zaimplementowano metody")

########################################################################

class AlgotyrmLFU(AlgorytmWymianyStron):

    def wybierz_strone(self) -> int:
        return 0
    
    def __str__(self) -> str:
        return "\nWyniki algorytmu LFU\n"

########################################################################

class AlgorytmMFU(AlgorytmWymianyStron):

    def wybierz_strone(self) -> int:
        return 0

    def __str__(self) -> str:
        return "\nWyniki algorytmu MFU\n"