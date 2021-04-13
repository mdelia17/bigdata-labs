#!/usr/bin/env python3
"""mapper.py"""

import sys
MISSING = 9999

for line in sys.stdin:
    line = line.strip()
    year = line[15:19]

    if line[87] not in {'+', '-'}:
        air_temperature = line[87:91]
    else:
        air_temperature = line[87:92]

    try:
        year = int(year)
        air_temperature = int(air_temperature)
    except ValueError:
        continue
    
    if air_temperature == MISSING:
        continue
    
    print("%i\t%i" % (year, air_temperature))