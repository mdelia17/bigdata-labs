#!/usr/bin/env python3
"""mapper.py"""

import sys

USER_ID = 0
TRACK_ID = 1
IS_SHARED = 2
RADIO = 3
IS_SKIPPED = 4

for line in sys.stdin:
    line = line.strip()
    bits = line.split("|")

    if len(bits) != 5:
        continue

    current_user_id = bits[USER_ID]
    current_track_id = bits[TRACK_ID]

    print("%s\t%s" % (current_track_id, current_user_id))