#!/usr/bin/env python3
"""spark application"""

import json
import argparse

from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")

args = parser.parse_args()
input_filepath = args.input_path

spark = SparkSession.builder.appName("Tweet Mining: all names mentions").config("spark.executor.memory", "500").getOrCreate()

lines_RDD = spark.sparkContext.textFile(input_filepath)

tweets_RDD = lines_RDD.map(f=lambda line: json.loads(line.strip()))

texts_RDD = tweets_RDD.map(f=lambda tweet: tweet["text"])

words_RDD = texts_RDD.map(f=lambda tweet_text: tweet_text.split(" "))

names_RDD = words_RDD.filter(f=lambda word: word.startswith("@") and len(word) > 1)

number_of_mentions = names_RDD.count()
print("\nMentioned names: %i\n" %number_of_mentions)