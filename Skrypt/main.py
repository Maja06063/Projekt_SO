from generator import Generator
from procesor import Procesor
import sys

if __name__ == "__main__":

    if "-g" in sys.argv:
        generator = Generator()
        generator.generuj ()

    if "-SJF" in sys.argv:
        print("dupa")
        procesor = Procesor(True)
        procesor.uszereguj_ciagi_zad()

    if "-LCFS" in sys.argv:
        procesor = Procesor(False)
        procesor.uszereguj_ciagi_zad()