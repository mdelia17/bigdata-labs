#!/usr/bin/env python3
"""mapper.py"""

import sys

DATE = 0
MIN = 1
MAX = 2

for line in sys.stdin:
    bits = line.strip().split(",")

    if len(bits) != 3:
        continue
    
    ddmmyyyy = bits[DATE]
    mmyyyy = ddmmyyyy[2:]
    max_temperature = bits[MAX]
    print("%s\t%s" % (mmyyyy, max_temperature))