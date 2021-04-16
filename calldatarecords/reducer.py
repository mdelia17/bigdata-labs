#!/usr/bin/env python3
"""reducer.py"""

import sys

caller_2_time = dict()

for line in sys.stdin:
    caller, milliseconds = line.strip().split("\t")
    milliseconds = int(milliseconds)

    if caller not in caller_2_time:
        caller_2_time[caller] = 0

    caller_2_time[caller] += milliseconds

for caller in caller_2_time:
    std_minutes = caller_2_time[caller]//60000
    if std_minutes >= 60:
        print("%s\t%i" % (caller, std_minutes))