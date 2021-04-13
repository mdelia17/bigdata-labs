#!/usr/bin/env python3
"""reducer.py"""

import sys

year_2_max_temperature = {}

for line in sys.stdin:
    line = line.strip()
    year, temperature = line.split("\t")
    
    try:
        year = int(year)
        temperature = int(temperature)
    except ValueError:
        continue

    if year not in year_2_max_temperature:
        year_2_max_temperature[year] = temperature
    else:
        if temperature > year_2_max_temperature[year]:
            year_2_max_temperature[year] = temperature

for year in year_2_max_temperature:
    print("%i\t%i" % (year, year_2_max_temperature[year]))