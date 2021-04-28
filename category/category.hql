CREATE TABLE docs (name STRING, category STRING, price FLOAT)
ROW FORMAT DELIMITED '\t'
FIELDS TERMINATED BY ' ';

LOAD DATA LOCAL INPATH 'category/catalog.txt' OVERWRITE INTO TABLE docs;

SELECT category, COUNT(*), AVG(price)
    FROM docs
    GROUP BY category;

DROP TABLE docs;