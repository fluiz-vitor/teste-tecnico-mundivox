.print '1. Qual time marcou mais gols na competição?'
SELECT time, SUM(gols) AS golsMarcados
FROM (
    SELECT time1 AS time, golsTime1 AS gols FROM partidas
    UNION ALL
    SELECT time2 AS time, golsTime2 AS gols FROM partidas
)
GROUP BY time
ORDER BY golsMarcados DESC
LIMIT 1;

.print ''
.print '2. Qual time sofreu menos gols na competição?'
SELECT time, SUM(gols) AS golsSofridos
FROM (
    SELECT time1 AS time, golsTime2 AS gols FROM partidas
    UNION ALL
    SELECT time2 AS time, golsTime1 AS gols FROM partidas
)
GROUP BY time
ORDER BY golsSofridos ASC
LIMIT 1;

.print ''
.print '3. Quantas partidas foram disputadas em cada fase?'
SELECT fase, COUNT(*) AS totalPartidas
FROM partidas
GROUP BY fase;

.print ''
.print '4. Quem foi o campeão da Copa do Mundo?'
SELECT vencedor AS campeao
FROM partidas
WHERE fase = 'Final';
