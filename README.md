# Teste Técnico Mundivox - Copa do Mundo 2026

Programa em Python que simula a fase eliminatória da Copa do Mundo 2026, das
oitavas de final até o campeão.

## Estrutura

```
src/
  main.py        -> roda a simulação e salva tudo no banco
  partida.py     -> uma partida (placar, prorrogação, pênaltis)
  torneio.py     -> controla as fases (oitavas, quartas, semi, final)
  banco.py       -> salva os dados no SQLite
  consultas.py   -> menu para consultar o banco
sql/
  criarTabelas.sql -> cria as tabelas do banco
  inserirDados.sql -> exemplo de como os dados são inseridos
  consultas.sql    -> consultas ao banco de dados
exemplos/
  entrada.json   -> times que compõem o confronto das oitavas
  saida.json     -> resultado de uma execução
copa.db          -> banco gerado quando o programa roda
```

## Como rodar

Para rodar o programa, só precisa do Python 3.

```bash
cd src
python3 main.py
```

Quando roda, o programa:

1. lê os confrontos das oitavas em `exemplos/entrada.json`
2. simula as fases até o campeão (os placares são sorteados aleatóriamente)
3. salva as 15 partidas no banco `copa.db`
4. salva o resultado em `exemplos/saida.json`

Como os placares são aleatórios, cada execução pode resultar em um campeão diferente.

## Entrada

O arquivo `exemplos/entrada.json` tem os 8 jogos das oitavas (16 times). As outras
fases o programa gera sozinho.

```json
{
  "oitavas": [
    ["Brasil", "Tunisia"],
    ["Argentina", "Mexico"],
    ["Portugal", "Senegal"],
    ["Alemanha", "Espanha"],
    ["França", "Croacia"],
    ["Holanda", "Suécia"],
    ["Inglaterra", "Estados Unidos"],
    ["Itália", "Bélgica"]
  ]
}
```

## Consultar o banco

Pelo Python (menu interativo):

```bash
cd src
python3 consultas.py
```

Ou use o SQLite.
Caso ainda não tenha instalado, rode o comando:

```bash
sudo apt install sqlite3
```

Para executar as consultas no banco de dados, rode o comando:

```bash
sqlite3 copa.db < sql/consultas.sql
```

## Tabelas do banco

- **times**: id, nome
- **partidas**: id, fase, time1, time2, golsTime1, golsTime2, prorrogacao, penaltis, vencedor

## Consultas que o .py faz

- Lista os times
- Busca partidas de um time
- Busca partidas de uma fase
- Estatísticas de um time
- Time que marcou mais gols
- Time que sofreu menos gols
- Quantas partidas por fase
- Campeão

## Consultas que o .sql faz

- Qual time marcou mais gols na competição
- Qual time sofreu menos gols na competição
- Quantas partidas foram disputadas em cada fase
- Quem foi o campeão


## Saída

A saída aparece no terminal e também é salva em `exemplos/saida.json`.

### No terminal

```
Oitavas de Final:
Brasil 1 x 10 Tunisia -> Tunisia
Argentina 7 x 3 Mexico -> Argentina
...

Quartas de Final:
Tunisia 8 x 0 Argentina -> Tunisia
...

Semi Final:
Tunisia 7 x 2 Senegal -> Tunisia
...

Final:
Tunisia 8 x 5 Estados Unidos -> Tunisia

Campeão: Tunisia

15 partidas salvas em copa.db
```

### No arquivo saida.json

```json
{
  "campeao": "Tunisia",
  "partidas": [
    {
      "fase": "Oitavas de Final",
      "time1": "Brasil",
      "time2": "Tunisia",
      "golsTime1": 1,
      "golsTime2": 10,
      "prorrogacao": false,
      "penaltis": false,
      "vencedor": "Tunisia"
    }
  ]
}
```# teste-tecnico-mundivox
