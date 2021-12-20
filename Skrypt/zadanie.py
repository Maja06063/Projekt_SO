class Zadanie:
    nr = 0
    t_wyk = 0
    t_nad = 0
    def __str__(self) -> str:
        return str(self.nr) + "\t" + str(self.t_wyk) + "\t" + str(self.t_nad)