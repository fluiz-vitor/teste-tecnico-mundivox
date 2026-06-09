import sqlite3
import os

CAMINHO_DB = os.path.join(os.path.dirname(__file__), "..", "copa.db")
SQL_DIR = os.path.join(os.path.dirname(__file__), "..", "sql")

class Banco:
    def __init__(self, caminho=CAMINHO_DB):
        self.conexao = sqlite3.connect(caminho)
        self.cursor = self.conexao.cursor()

    def criarTabelas(self):
        with open(os.path.join(SQL_DIR, "criarTabelas.sql"), encoding="utf-8") as f:
            self.cursor.executescript(f.read())
        self.cursor.execute("DELETE FROM partidas")
        self.cursor.execute("DELETE FROM times")
        self.conexao.commit()

    def salvarTime(self, nome):
        self.cursor.execute("INSERT OR IGNORE INTO times (nome) VALUES (?)", (nome,))

    def salvarPartida(self, partida):
        self.salvarTime(partida.time1)
        self.salvarTime(partida.time2)
        self.cursor.execute(
            """INSERT INTO partidas
               (fase, time1, time2, golsTime1, golsTime2, prorrogacao, penaltis, vencedor)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (partida.fase, partida.time1, partida.time2, partida.golsTime1, partida.golsTime2,
             int(partida.prorrogacao), int(partida.penaltis), partida.vencedor),
        )

    def commit(self):
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()
