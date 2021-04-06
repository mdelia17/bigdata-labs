#!/bin/bash

# script to format namenode

echo 'format namenode...'
$HADOOP_HOME/bin/hdfs namenode -format
