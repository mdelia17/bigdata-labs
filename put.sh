#!/bin/bash

# script to put file on hdfs $1 is path of the file

if [ $# -eq 0 ]; then
    echo "No path of input file provided"
    exit 1
fi
$HADOOP_HOME/bin/hdfs dfs -put bigdata/$1 input
