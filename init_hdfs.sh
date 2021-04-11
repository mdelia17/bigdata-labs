#!/bin/bash

# script to create the HDFS directories required to execute MapReduce jobs
echo 'creating the HDFS directories required to execute MapReduce jobs...'
$HADOOP_HOME/bin/hdfs dfs -mkdir /user
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/marco
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/marco/input
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/marco/output
