#!/usr/bin/env python3
"""mapper.py"""

import sys
import re

for line in sys.stdin:
    line = line.strip()
    tokens = re.split("[/\\\_|$#<>^=,;.:()?!'\"*\[\]\-\s0-9]", line)
    tokens = list(filter(None, tokens))

    for token in tokens:
        print("%s\t%i" % (token.lower(), 1))