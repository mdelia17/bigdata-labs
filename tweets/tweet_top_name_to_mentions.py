#!/usr/bin/env python3
"""spark application"""

import json
import argparse
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output path", type=str, help="Output folder path")

args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_filepath

spark = SparkSession.builder.appName("Tweet Mining: top name to mentions").config("spark.executor.memory", "500").getOrCreate()

lines_RDD = spark.sparkContext.textFile(input_filepath)

tweets_RDD = lines_RDD.map(f=lambda line: json.loads(line.strip()))

texts_RDD = tweets_RDD.map(f=lambda tweet: tweet["text"])

words_RDD = texts_RDD.flatMap(f=lambda tweet_text: tweet_text.split(" "))

names_RDD = words_RDD.filter(f=lambda word: word.startswith("@") and len(word) > 1)

name_to_one_RDD = names_RDD.map(f=lambda name: (name, 1))

name_to_count_RDD = name_to_one_RDD.reduceByKey(func= lambda a, b: a+b)

sorted_name_to_count_RDD = name_to_count_RDD.sortBy(keyfunc=lambda name_with_count : name_with_count[1], ascending=False)

top_name_count_pairs = sorted_name_to_count_RDD.take(10)

top_name_to_count_RDD = spark.sparkContext.parallelize(top_name_count_pairs)

top_name_to_count_RDD.saveAsTextFile(output_filepath)