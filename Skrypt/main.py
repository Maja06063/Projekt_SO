from generator import Generator
from procesor import *
import sys

if __name__ == "__main__":

    generator = Generator()
    procesorSJF = Procesor(AlgorytmSJF())
    procesorLCFS = Procesor(AlgotyrmLCFS())

    if "-g" in sys.argv:
        generator.generuj (False)
        generator.generuj(True)

    if "-SJF" in sys.argv:   
        procesorSJF.uszereguj_ciagi_zad()

    if "-LCFS" in sys.argv:
        procesorLCFS.uszereguj_ciagi_zad()