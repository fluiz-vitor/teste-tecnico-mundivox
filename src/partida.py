import random

class Partida:
    def __init__(self, fase, time1, time2):
        self.fase = fase
        self.time1 = time1
        self.time2 = time2
        self.golsTime1 = 0
        self.golsTime2 = 0
        self.prorrogacao = False
        self.penaltis = False
        self.vencedor = None


    def jogar(self):
        self.golsTime1 = random.randint(0, 10)
        self.golsTime2 = random.randint(0, 10)

        if self.golsTime1 > self.golsTime2:
            self.vencedor = self.time1
        elif self.golsTime2 > self.golsTime1:
            self.vencedor = self.time2
        else:
            self.prorrogacao = True
            self.jogar()
            if self.golsTime1 > self.golsTime2:
                self.vencedor = self.time1
            elif self.golsTime2 > self.golsTime1:
                self.vencedor = self.time2
            else:
                self.penaltis = True
                self.jogar()
                if self.golsTime1 > self.golsTime2:
                    self.vencedor = self.time1
                elif self.golsTime2 > self.golsTime1:
                    self.vencedor = self.time2

    def placarTexto(self):
        return f"{self.time1} {self.golsTime1} x {self.golsTime2} {self.time2}"
    