import json
import os
from torneio import Torneio
from banco import Banco

BASE = os.path.dirname(__file__)
ENTRADA = os.path.join(BASE, "..", "exemplos", "entrada.json")
SAIDA = os.path.join(BASE, "..", "exemplos", "saida.json")


def main():
    with open(ENTRADA, encoding="utf-8") as f:
        dados = json.load(f)
    confrontos = dados["oitavas"]

    torneio = Torneio(confrontos)
    campeao = torneio.simular()

    banco = Banco()
    banco.criarTabelas()
    for p in torneio.partidas:
        banco.salvarPartida(p)
    banco.commit()
    banco.fechar()
    print(f"\n{len(torneio.partidas)} partidas salvas em copa.db")

    partidas = []
    for p in torneio.partidas:
        partidas.append({
            "fase": p.fase,
            "time1": p.time1,
            "time2": p.time2,
            "golsTime1": p.golsTime1,
            "golsTime2": p.golsTime2,
            "prorrogacao": p.prorrogacao,
            "penaltis": p.penaltis,
            "vencedor": p.vencedor,
        })

    resultado = {"campeao": campeao, "partidas": partidas}
    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
