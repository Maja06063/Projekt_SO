from zadanie import Zadanie

class AlgorytmSzereg:

    def wybierz_zadanie(self, dostepne_zadania) -> Zadanie:
        raise NotImplementedError("Błąd - nie zaimplementowano metody")

########################################################################

class AlgotyrmLCFS(AlgorytmSzereg):

    def wybierz_zadanie(self, dostepne_zadania) -> Zadanie:
        
        dostepne_zadania.sort(key=lambda zadanie: zadanie.t_nad)
        return dostepne_zadania[-1]

########################################################################

class AlgorytmSJF(AlgorytmSzereg):

    def wybierz_zadanie(self, dostepne_zadania) -> Zadanie:
        
        dostepne_zadania.sort(key=lambda zadanie: zadanie.t_wyk)
        return dostepne_zadania[0]