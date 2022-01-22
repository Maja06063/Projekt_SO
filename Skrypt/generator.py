from ustawienia import *
from zadanie import Zadanie
import random

"""
Klasa Generator służy do wygenerowania i zapisania do pliku zadań oraz numerów stron.
"""

class Generator:

    """
    Metoda zapisz_liste_ciag służy do zapisania do pliku podanej listy zadań lub stron.
    
    Argumenty: 
    list_ciag_zad - Lista, w której znajdują się zadania lub numery stron,
    nazwa_pliku - Nazwa pliku do zapisu danych

    Zwraca:
    Metoda nic nie zwraca
    """

    def zapisz_liste_ciag (self, list_ciag_zad, nazwa_pliku):
        plik = open(nazwa_pliku, "w")
        for ciag in list_ciag_zad:
            for zadanie_lub_strona in ciag:
                plik.write(str(zadanie_lub_strona) + "\n")
        plik.close()

    ########################################################################

    """
    Metoda generuj_zad służy do wygenerowania pojedyńczego zadania
    z losowym czasem wykonywania i czasem nadejścia.
    
    Argumenty: 
    Metoda nie przyjmuje żadnych argumentów.

    Zwraca:
    Metoda zwraca wygenerowane zadanie.
    """

    def generuj_zad (self)-> Zadanie:
        zad = Zadanie ()
        zad.t_nad = random.randint(0,400)
        zad.t_wyk = random.randint(1,20)
        return zad

    ########################################################################

    """
    Metoda generuj_str służy do wygenerowania pojedyńczego numeru strony.
    
    Argumenty: 
    Metoda nie przyjmuje żadnych argumentów.

    Zwraca:
    Metoda zwraca wylosowany numer strony.
    """

    def generuj_str (self)-> int:
        numer_strony=random.randint(1,LICZBA_STRON)
        return numer_strony

    ########################################################################

    """
    Metoda generuj służy do wywołania odpowiednich metod generujących i zapisujących do pliku
    zadania lub strony. Jest to główna metoda klasy Generator.
    
    Argumenty: 
    czy_strony - jeśli prawda to generuje strony, jeśli fałsz to generuje zadanie.

    Zwraca:
    Metoda nic nie zwraca
    """

    def generuj (self,czy_strony): 
        list_ciagow = []
        for i in range(0, ILOSC_CIAGOW):
            if czy_strony:
                ciag_stron = []
                for j in range(0, ILOSC_STRON_W_CIAGU):
                    nowe_zad = self.generuj_str ()
                    ciag_stron.append(nowe_zad)
                list_ciagow.append(ciag_stron)
            else:       
                ciag_zadan = []
                for j in range(0, ILOSC_ZADAN_W_CIAGU):
                    nowe_zad = self.generuj_zad ()
                    ciag_zadan.append(nowe_zad)
                list_ciagow.append(ciag_zadan)
        if czy_strony:
            self.zapisz_liste_ciag (list_ciagow,"lista_ciagow_stron.txt")
        else:
            self.zapisz_liste_ciag (list_ciagow,"lista_ciagow_zadan.txt")