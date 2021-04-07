#!/usr/bin/env python3
"""reducer.py"""

import sys

bigram_2_sum = {}

for line in sys.stdin:
    line = line.strip()
    cur_word_1, cur_word_2, cur_count = line.split("\t")
    cur_bigram = (cur_word_1, cur_word_2)

    try:
        cur_count = int(cur_count)
    except ValueError:
        continue

    if cur_bigram not in bigram_2_sum:
        bigram_2_sum[cur_bigram] = 0

    bigram_2_sum[cur_bigram] += cur_count

for bigram in bigram_2_sum:
    word_1, word_2 = bigram
    print("%s, %s: %i" % (word_1, word_2, bigram_2_sum[bigram]))