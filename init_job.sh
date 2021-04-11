#!/bin/bash

# script to init all files for a mapreduce job | $1 is the folder of the mapreduce job
if [ $# -eq 0 ]; then
    echo "No job name provided"
    exit 1
fi

mkdir $1
echo "folder for $1 job created"
cd $1

touch mapper.py
echo "#!/usr/bin/env python3" >> mapper.py
echo "\"\"\"mapper.py\"\"\"" >> mapper.py
echo "mapper.py created"

touch reducer.py
echo "#!/usr/bin/env python3" >> reducer.py
echo "\"\"\"reducer.py\"\"\"" >> reducer.py
echo "reducer.py created"

