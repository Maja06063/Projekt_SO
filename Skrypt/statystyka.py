class Statystyka:

    czas_spoznienia = []
    czas_cyklu = []

    def __init__(self):
        self.czas_spoznienia.clear()
        self.czas_cyklu.clear()

    def sredni_czas_spoznienia(self) -> float:
        return sum(self.czas_spoznienia) / len(self.czas_spoznienia)

    def sredni_czas_cyklu(self) -> float:
        return sum(self.czas_cyklu) / len(self.czas_cyklu)

    def __str__(self) -> str:
        return " Średni czas spóźnienia: " + str(self.sredni_czas_spoznienia()) + \
            "\n Średni czas cyklu: " + str(self.sredni_czas_cyklu())