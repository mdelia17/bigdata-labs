#!/bin/bash

FILE=/$1/$2

usage()
{
	echo "Usage: mapreduce.sh <mapreduce job> <input file in hdfs>"
	exit 1
}

missing_input()
{
	echo "Wrong input file!"
	exit 1
}

missing_mr()
{
	echo "Mapper and/or Reducer are/is missing!"
	exit 1
}

if [ $# -eq 0 ]; then
    usage
fi

if ! [ -f "$1/$2" ]; then
	missing_input
fi

if ! { [ -f "$1/mapper.py" ] && [ -f "$1/reducer.py" ]; }; then
	missing_mr
fi

$HADOOP_HOME/bin/hdfs dfs -put bigdata/$1/$2 input

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/streaming/hadoop-streaming-3.2.2.jar -mapper ~/bigdata/$1/mapper.py -reducer ~/bigdata/$1/reducer.py -input /user/marco/input/$2 -output /user/marco/output/$1


