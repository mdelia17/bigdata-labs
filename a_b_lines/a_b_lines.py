#!/usr/bin/env python3
"""spark application"""

import argparse
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", type=str, help="Input file path")
parser.add_argument("--output_path", type=str, help="Output folder path")

args = parser.parse_args()
input_filepath, output_filepath = args.input_path, args.output_path

spark = SparkSession.builder.appName("Python Spark basic example").getOrCreate()

input_RDD = spark.sparkContext.textFile(input_filepath)

def contains_a(line):
    return 'a' in line

def contains_b(line):
    return 'b' in line

a_lines_RDD = input_RDD.filter(contains_a)
b_lines_RDD = input_RDD.filter(contains_b)

num_a = a_lines_RDD.count()
num_b = b_lines_RDD.count()

output_string = "Lines with a: %i, lines with b: %i" % (num_a, num_b)
spark.sparkContext.parallelize([output_string]).saveAsTextFile(output_filepath)