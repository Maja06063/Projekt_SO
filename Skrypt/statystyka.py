class Statystyka:

    def __init__(self):
        self.czas_spoznienia = []
        self.czas_cyklu = [] 
        self.ilosc_podmian_stron = []

    def sredni_czas_spoznienia(self) -> float:
        return sum(self.czas_spoznienia) / len(self.czas_spoznienia)

    def sredni_czas_cyklu(self) -> float:
        return sum(self.czas_cyklu) / len(self.czas_cyklu)

    def __str__(self) -> str:
        return str(self.sredni_czas_spoznienia()) + \
            ";"  + str(self.sredni_czas_cyklu())

    def srednia_ilosc_podmian_stron (self) -> float:
        return sum(self.ilosc_podmian_stron) / len(self.ilosc_podmian_stron)