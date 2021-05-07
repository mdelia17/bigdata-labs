#!/usr/bin/env python3
"""spark application"""

import argparse
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output_path", type=str, help="Output folder path")

args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_path

spark = SparkSession.builder.appName("Spark Wordcount").getOrCreate()

lines_RDD = spark.sparkContext.textFile(input_filepath).cache()

words_RDD = lines_RDD.flatMap(f=lambda line: line.strip().split(" "))

word_2_one_RDD = words_RDD.map(f=lambda word: (word, 1))

word_2_count_RDD = word_2_one_RDD.reduceByKey(func=lambda a, b: a + b)

output_strings_RDD = word_2_count_RDD.map(f=lambda word_count_pair: "%s: %i" %(word_count_pair[0], word_count_pair[1]))

output_strings_RDD.saveAsTextFile(output_filepath)