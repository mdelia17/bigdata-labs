#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")

    for i in range(len(words)-1):
        print('%s\t%s\t%i' % (words[i], words[i+1], 1))