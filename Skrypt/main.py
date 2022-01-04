from generator import Generator
from procesor import Procesor
import sys

if __name__ == "__main__":

    generator = Generator()
    procesorSJF = Procesor(True)
    procesorLCFS = Procesor(False)

    if "-g" in sys.argv:
        generator.generuj ()

    if "-SJF" in sys.argv:   
        procesorSJF.uszereguj_ciagi_zad()

    if "-LCFS" in sys.argv:
        procesorLCFS.uszereguj_ciagi_zad()