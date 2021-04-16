#!/usr/bin/env python3
"""reducer.py"""

import sys

def mean(items_list):
    s = 0.0
    for item in items_list:
        s += item
    return s/float(len(items_list))

month_2_max_temps = dict()

for line in sys.stdin:
    month, max_temp = line.strip().split("\t")

    if month not in month_2_max_temps:
        month_2_max_temps[month] = []

    month_2_max_temps[month].append(float(max_temp))

for month in month_2_max_temps:
    mean_max_temp = mean(month_2_max_temps[month])
    print("%s\t%f" % (month, mean_max_temp))