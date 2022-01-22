
from generator import Generator
from procesor import *
import sys

"""
Główna funkcja programu. Parsuje dostępne opcje i uruchamia funkcje algorytmów.
Nie może być wywołana z innego skryptu.
"""

if __name__ == "__main__":

    pelny_przebieg = False
    if "-a" in sys.argv:
        pelny_przebieg = True

    if "-g" in sys.argv or pelny_przebieg:
        generator = Generator()
        generator.generuj (False)
        generator.generuj(True)

    if "-SJF" in sys.argv or pelny_przebieg:
        procesorSJF = Procesor(AlgorytmSJF())  
        procesorSJF.uszereguj_ciagi_zad()

    if "-LCFS" in sys.argv or pelny_przebieg:
        procesorLCFS = Procesor(AlgotyrmLCFS())
        procesorLCFS.uszereguj_ciagi_zad()
    
    if "-MFU" in sys.argv or pelny_przebieg:
        procesorMFU = Procesor(AlgorytmMFU())
        procesorMFU.uszereguj_ciagi_stron()

    if "-LFU" in sys.argv or pelny_przebieg:
        procesorLFU = Procesor(AlgotyrmLFU())
        procesorLFU.uszereguj_ciagi_stron()

    if "-h" in sys.argv or len(sys.argv) < 2:
        print(POMOC)