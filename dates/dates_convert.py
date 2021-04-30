#!/usr/bin/env python3
import sys
from datetime import datetime

OUTPUT_FORMAT = '%Y-%m-%d %H:%M:%S'

for line in sys.stdin:
    line = line.strip()
    name, unix_date = line.split("\t")

    try:
        unix_date = int(unix_date)
    except ValueError:
        continue

    datetime_obj = datetime.utcfromtimestamp(unix_date)
    out_date_str = datetime_obj.strftime(OUTPUT_FORMAT)
    print("\t".join([name, out_date_str]))