#!/usr/bin/env python3
"""reducer.py"""

import sys

inverted_index = {}

for line in sys.stdin:
    line = line.strip()
    word, sentence_number_str = line.split("\t")

    if word not in inverted_index:
        inverted_index[word] = set()

    inverted_index[word].add(sentence_number_str)

for word in inverted_index:
    print(word + "\t" + "[" + ", ".join(inverted_index[word]) + "]")