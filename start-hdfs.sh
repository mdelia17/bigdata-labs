#!/bin/bash

#script to start dfs

rm -Rf /tmp/hadoop-marco/
rm -Rf /tmp/hadoop-yarn-marco/

echo 'formatting namenode...'
$HADOOP_HOME/bin/hdfs namenode -format

echo 'running start-dfs.sh'
$HADOOP_HOME/sbin/start-dfs.sh
