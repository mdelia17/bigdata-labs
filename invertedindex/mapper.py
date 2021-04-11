#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    sentence_number, sentence = line.split("\t")
    words = sentence.split(" ")

    try:
        sentence_number = int(sentence_number)
    except ValueError:
        continue

    for word in words:
        print("%s\t%i" % (word, sentence_number))