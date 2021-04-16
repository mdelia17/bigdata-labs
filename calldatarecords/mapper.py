#!/usr/bin/env python3
"""mapper.py"""

import sys
from datetime import datetime

FROM_PHONE_NUMBER = 0
TO_PHONE_NUMBER = 1
CALL_START_TIME = 2
CALL_END_TIME = 3
STD_FLAG = 4

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

def to_millis(date_string):
    timestamp = datetime.strptime(date_string, TIMESTAMP_FORMAT)
    return timestamp.timestamp() * 1000

for line in sys.stdin:
    bits = line.strip().split("|")

    if len(bits) != 5:
        continue
    
    if int(bits[STD_FLAG]) == 1:
        caller = int(bits[FROM_PHONE_NUMBER])
        start_millis  = to_millis(bits[CALL_START_TIME])
        end_millis = to_millis(bits[CALL_END_TIME])
        print("%i\t%i" % (caller, end_millis - start_millis))