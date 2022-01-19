from xmlrpc.client import Boolean


class Ramka:
    rozmiar = 0

    def __init__(self,rozmiar) -> None:
        self.rozmiar = rozmiar
        self.miejsce_w_ramce = [3]

    def zmien_strone(self,numer_miejsca_w_ramce,strona):
        self.miejsce_w_ramce[numer_miejsca_w_ramce] = strona

    def czy_zawiera(self,strona) -> Boolean:
        return strona in self.miejsce_w_ramce