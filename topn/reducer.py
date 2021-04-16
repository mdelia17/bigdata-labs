#!/usr/bin/env python3
"""reducer.py"""

import sys

token_2_frequency = dict()

for line in sys.stdin:
    token, value = line.strip().split("\t")

    if token not in token_2_frequency:
        token_2_frequency[token] = 0

    token_2_frequency[token] += int(value)

tokens_with_frequencies = token_2_frequency.items()
sorted_tokens_with_frequencies = sorted(tokens_with_frequencies,
                                        key=lambda item: item[1],
                                        reverse=True)
top_20_tokens_with_frequencies = sorted_tokens_with_frequencies[:20]

for (token, frequency) in top_20_tokens_with_frequencies:
    print("%s\t%i" % (token, frequency))