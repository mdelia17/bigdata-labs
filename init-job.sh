#!/bin/bash

usage()
{
	echo "Usage: init_job.sh <name of the job>"
	exit 1
}

if [ $# -eq 0 ]; then
    usage
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

