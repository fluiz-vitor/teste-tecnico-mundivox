from partida import Partida

class Torneio:
    def __init__(self, times):
        self.times = times
        self.partidas = []

    def jogarFasesEliminatorias(self, fase, confronto):
        vencedores = []
        print(f"{fase}:")
        for time1, time2 in confronto:
            partida = Partida(fase, time1, time2)
            partida.jogar()
            self.partidas.append(partida)
            vencedores.append(partida.vencedor)
            print(f"{partida.placarTexto()} -> {partida.vencedor}")
        return vencedores

    def montarConfrontos(self, times):
        return [(times[i], times[i+1]) for i in range(0, len(times), 2)]

    def simular(self):
        # os confrontos das oitavas já vêm em pares (vindos do entrada.json)
        times = self.jogarFasesEliminatorias("Oitavas de Final", self.times)
        print('')
        times = self.jogarFasesEliminatorias("Quartas de Final", self.montarConfrontos(times))
        print('')
        times = self.jogarFasesEliminatorias("Semi Final", self.montarConfrontos(times))
        print('')
        campeao = self.jogarFasesEliminatorias("Final", self.montarConfrontos(times))[0]
        print(f"\nCampeão: {campeao}")
        return campeao