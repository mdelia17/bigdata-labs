CREATE TABLE user_docs (username STRING, webpage STRING, time STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

CREATE TABLE page_docs (webpage STRING, page_rank FLOAT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH 'pagerank/visits.log' OVERWRITE INTO TABLE user_docs;

LOAD DATA LOCAL INPATH 'pagerank/pages.log' OVERWRITE INTO TABLE page_docs;

CREATE TABLE user_visit_ranks AS
    SELECT username, AVG(page_rank) AS user_visit_ranks
    FROM user_docs join page_docs  
        ON (user_docs.webpage = page_docs.webpage)
    GROUP BY username;

SELECT * FROM user_visit_ranks WHERE user_rank > 0.5;

DROP TABLE user_docs;
DROP TABLE page_docs;
DROP TABLE user_visit_ranks;