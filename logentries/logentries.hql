CREATE TABLE docs (user_id STRING, time STRING, query STRING)
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH 'logentries/excite-small.log' OVERWRITE INTO TABLE docs;

SELECT * FROM docs LIMIT 10;

CREATE TABLE user_counts AS
    SELECT user_id, count(*)
    FROM docs
    GROUP BY user_id;

SELECT * FROM user_counts ORDER_BY user_id;

DROP TABLE docs;
DROP TABLE user_counts;
