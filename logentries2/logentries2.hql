CREATE TABLE docs (user_id STRING, time STRING, query STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH 'logentries2/visits.log' OVERWRITE INTO TABLE docs;

SELECT * FROM docs;

CREATE TABLE user_visits AS
    SELECT user_id, count (*) AS visit_number
    FROM docs
    GROUP BY user_id;

SELECT AVG(visit_number)
FROM user_visits;

DROP TABLE docs;
DROP TABLE user_visits;