CREATE TABLE docs (receipt_id INT, item_id INT)
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH 'marketbasket/purchase.txt' OVERWRITE INTO TABLE docs;

SELECT d1.item_id AS item_1, d2.item_id as item_2, COUNT(*)
FROM
    (SELECT DISTINCT receipt_id, item_id FROM docs) AS d1
    JOIN
    (SELECT DISTINCT receipt_id, item_id FROM docs) AS d2
    ON (d1.receipt_id = d2.receipt_id)
GROUP BY d1.item_id, d2.item_id
HAVING d1.item_id != d2.item_id;

DROP TABLE docs;