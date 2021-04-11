#!/bin/bash

# script to run a mapreduce job | $1 is the folder of the mapreduce job | $2 is the input file in hdfs
if [ $# -eq 0 ]; then
    echo "No path of mapper/reducer and input file provided"
    exit 1
fi
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/streaming/hadoop-streaming-3.2.2.jar -mapper ~/bigdata/$1/mapper.py -reducer ~/bigdata/$1/reducer.py -input /user/marco/input/$2 -output /user/marco/output/$1
