#!/bin/bash

usage()
{
	echo "Usage: spark-yarn.sh <spark job> <input file in hdfs>"
	exit 1
}

missing_input()
{
	echo "Wrong input file!"
	exit 1
}

missing_spark()
{
	echo "spark.py is missing!"
	exit 1
}

if [ $# -eq 0 ]; then
    usage
fi

if ! [ -f "$1/$2" ]; then
	missing_input
fi

if ! [ -f "$1/spark.py" ]; then
	missing_spark
fi

$HADOOP_HOME/bin/hdfs dfs -put bigdata/$1/$2 input

$SPARK_HOME/bin/spark-submit --master yarn ~/bigdata/$1/spark.py --input_path hdfs:///user/marco/input/$2 --output_path hdfs:///user/marco/output/$1
