#!/usr/bin/env python3
"""reducer.py"""

import sys

# these dictionary map each letter to the number of the corresponding
# words and to the sum of their lengths, as obtained from the mapper output
letter_2_word_count = {}
letter_2_word_lengths_sum = {}

for line in sys.stdin:
    line = line.strip()
    letter, word_length = line.split("\t")

    try:
        word_length = int(word_length)
    except ValueError:
        continue

    if letter not in letter_2_word_count:
        letter_2_word_count[letter] = 0
        letter_2_word_lengths_sum[letter] = 0
    
    letter_2_word_count[letter] += 1
    letter_2_word_lengths_sum[letter] += word_length

for letter in letter_2_word_count:
    average_word_length = float(letter_2_word_lengths_sum[letter])/\
                        float(letter_2_word_count[letter])
    print("%s\t%f" % (letter, average_word_length))