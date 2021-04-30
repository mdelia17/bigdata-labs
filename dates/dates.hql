CREATE TABLE subscribers_docs (name STRING, deparment INT, email STRING, unix_time STRING)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH 'dates/subscribers.txt'
    OVERWRITE INTO TABLE subscribers_docs;

ADD FILE dates/date_convert.py;

CREATE TABLE subscribers AS
    SELECT TRANSFORM(subscribers_docs.name, subscribers_docs.unix_time)
        USING 'python3 dates/date_convert.py'
        AS name, converted_time
        FROM subscribers_docs;

SELECT * FROM subscribers;

DROP TABLE subscribers_docs;
DROP TABLE subscribers;
