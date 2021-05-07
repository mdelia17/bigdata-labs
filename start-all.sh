#!/bin/bash

#script to start yarn resource manager daemons

rm -Rf /tmp/hadoop-marco/
rm -Rf /tmp/hadoop-yarn-marco/

echo 'formatting namenode...'
$HADOOP_HOME/bin/hdfs namenode -format

echo 'running start-all.sh'
$HADOOP_HOME/sbin/start-all.sh
