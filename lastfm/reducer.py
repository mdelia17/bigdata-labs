#!/usr/bin/env python3
"""reducer.py"""

import sys

track_2_users = dict()

for line in sys.stdin:
    line = line.strip()
    current_track, current_user = line.split("\t")

    if current_track not in track_2_users:
        track_2_users[current_track] = set()

    track_2_users[current_track].add(current_user)

for track in track_2_users:
    print("%s\t%i" % (track, len(track_2_users[track])))