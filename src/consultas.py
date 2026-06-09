import sqlite3
import os

CAMINHO_DB = os.path.join(os.path.dirname(__file__), "..", "copa.db")


class Consultas:
    def __init__(self, caminho=CAMINHO_DB):
        self.conexao = sqlite3.connect(caminho)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

    def listarTimes(self):
        self.cursor.execute("SELECT nome FROM times ORDER BY nome")
        times = [linha[0] for linha in self.cursor.fetchall()]
        print(f"\n{len(times)} times na competição:")
        for nome in times:
            print(f"  - {nome}")

    def partidasDoTime(self, time):
        self.cursor.execute(
            """SELECT fase, time1, golsTime1, golsTime2, time2, vencedor
               FROM partidas
               WHERE time1 = ? OR time2 = ?
               ORDER BY id""",
            (time, time),
        )
        linhas = self.cursor.fetchall()
        if not linhas:
            print(f"\nNenhuma partida encontrada para esse time.")
            return
        print(f"\nPartidas {time}:")
        for fase, t1, g1, g2, t2, venc in linhas:
            print(f"  [{fase}] {t1} {g1} x {g2} {t2}  -> {venc}")

    def partidasDaFase(self, fase):
        self.cursor.execute(
            """SELECT time1, golsTime1, golsTime2, time2, vencedor
               FROM partidas
               WHERE fase = ?
               ORDER BY id""",
            (fase,),
        )
        linhas = self.cursor.fetchall()
        if not linhas:
            print(f"\nNenhuma partida encontrada na fase '{fase}'.")
            return
        print(f"\nPartidas da(s) {fase}:")
        for t1, g1, g2, t2, venc in linhas:
            print(f"  {t1} {g1} x {g2} {t2}  -> {venc}")

    def estatisticasDoTime(self, time):
        self.cursor.execute(
            "SELECT time1, golsTime1, golsTime2 FROM partidas WHERE time1 = ? OR time2 = ?",
            (time, time),
        )
        linhas = self.cursor.fetchall()
        if not linhas:
            print(f"\nTime '{time}' não encontrado.")
            return

        marcados = 0
        sofridos = 0
        for time1, golsTime1, golsTime2 in linhas:
            if time1 == time:
                marcados += golsTime1
                sofridos += golsTime2
            else:
                marcados += golsTime2
                sofridos += golsTime1

        print(f"\nEstatísticas de {time}:")
        print(f"  Jogos disputados: {len(linhas)}")
        print(f"  Gols marcados:    {marcados}")
        print(f"  Gols sofridos:    {sofridos}")

    def campeao(self):
        self.cursor.execute("SELECT vencedor FROM partidas WHERE fase = 'Final'")
        linha = self.cursor.fetchone()
        if linha:
            print(f"\n🏆 Campeão: {linha[0]}")
        else:
            print("\nFinal ainda não disputada.")

    def maisGols(self):
        self.cursor.execute(
            """SELECT time, SUM(gols) AS total FROM (
                   SELECT time1 AS time, golsTime1 AS gols FROM partidas
                   UNION ALL
                   SELECT time2 AS time, golsTime2 AS gols FROM partidas
               ) GROUP BY time ORDER BY total DESC LIMIT 1"""
        )
        time, total = self.cursor.fetchone()
        print(f"\nMaior ataque: {time} ({total} gols marcados)")

    def menosSofridos(self):
        self.cursor.execute(
            """SELECT time, SUM(gols) AS total FROM (
                   SELECT time1 AS time, golsTime2 AS gols FROM partidas
                   UNION ALL
                   SELECT time2 AS time, golsTime1 AS gols FROM partidas
               ) GROUP BY time ORDER BY total ASC LIMIT 1"""
        )
        time, total = self.cursor.fetchone()
        print(f"\nMelhor defesa: {time} ({total} gols sofridos)")

    def partidasPorFase(self):
        self.cursor.execute(
            "SELECT fase, COUNT(*) FROM partidas GROUP BY fase ORDER BY MIN(id)"
        )
        print("\nPartidas por fase:")
        for fase, total in self.cursor.fetchall():
            print(f"  {fase}: {total}")


MENU = """
CONSULTAS DA COPA DO MUNDO 2026

1 - Listar times
2 - Buscar partidas de um time
3 - Buscar partidas de uma fase
4 - Estatísticas de um time
5 - Time que marcou mais gols
6 - Time que sofreu menos gols
7 - Quantas partidas por fase
8 - Campeão
0 - Sair
"""


def formatar(texto):
    return texto.strip().title().replace(" De ", " de ")

def main():
    if not os.path.exists(CAMINHO_DB):
        print("Banco copa.db não encontrado. Rode primeiro: python3 main.py")
        return

    consultas = Consultas()
    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            break
        elif opcao == "1":
            consultas.listarTimes()
        elif opcao == "2":
            consultas.partidasDoTime(formatar(input("Nome do time: ")))
        elif opcao == "3":
            consultas.partidasDaFase(formatar(input("Nome da fase: ")))
        elif opcao == "4":
            consultas.estatisticasDoTime(formatar(input("Nome do time: ")))
        elif opcao == "5":
            consultas.maisGols()
        elif opcao == "6":
            consultas.menosSofridos()
        elif opcao == "7":
            consultas.partidasPorFase()
        elif opcao == "8":
            consultas.campeao()
        else:
            print("Opção inválida.")

    consultas.fechar()
    print("Até mais!")


if __name__ == "__main__":
    main()
