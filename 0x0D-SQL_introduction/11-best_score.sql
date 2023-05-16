-- Lists all records with >= 10 in second_table
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
