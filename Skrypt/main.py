
from generator import Generator
from procesor import *
import sys

if __name__ == "__main__":

    generator = Generator()
    procesorSJF = Procesor(AlgorytmSJF())
    procesorLCFS = Procesor(AlgotyrmLCFS())
    procesorMFU = Procesor(AlgorytmMFU())
    procesorLFU = Procesor(AlgotyrmLFU())

    if "-g" in sys.argv:
        generator.generuj (False)
        generator.generuj(True)

    if "-SJF" in sys.argv:   
        procesorSJF.uszereguj_ciagi_zad()

    if "-LCFS" in sys.argv:
        procesorLCFS.uszereguj_ciagi_zad()
    
    if "-MFU" in sys.argv:
        procesorMFU.uszereguj_ciagi_stron()

    if "-LFU" in sys.argv:
        procesorLFU.uszereguj_ciagi_stron()
