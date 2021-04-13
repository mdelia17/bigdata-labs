CREATE TABLE docs (line String);
LOAD DATA LOCAL INPATH 'wordcount/words.txt' OVERWRITE INTO TABLE docs;

SELECT * FROM docs;

CREATE TABLE word_counts AS
    SELECT exploded_line.word, count(*)
    FROM
        (SELECT explode(split(line, ' ')) AS word
         FROM docs) AS exploded_line
    GROUP BY exploded_line.word;

SELECT * FROM word_counts ORDER BY word;

DROP TABLE docs;
DROP TABLE word_counts;
