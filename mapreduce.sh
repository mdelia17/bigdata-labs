#!/bin/bash

usage()
{
	echo "Usage: mapreduce.sh <mapreduce job> <input file in hdfs>"
	exit 1
}

if [ $# -eq 0 ]; then
    usage
fi

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/streaming/hadoop-streaming-3.2.2.jar -mapper ~/bigdata/$1/mapper.py -reducer ~/bigdata/$1/reducer.py -input /user/marco/input/$2 -output /user/marco/output/$1


