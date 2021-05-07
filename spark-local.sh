#!/bin/bash

usage()
{
	echo "Usage: spark-local.sh <spark job> <input file in filesystem>"
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

$SPARK_HOME/bin/spark-submit --master local ./$1/spark.py --input_path file:///home/marco/bigdata/$1/$2 --output_path file:///home/marco/bigdata/$1/output
