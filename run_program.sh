#!/bin/bash

# Check if the user passed in the correct number of arguments
if [ $# -ne 1 ]; then
    echo "Usage: run_program.sh <pdf_file_path>"
    exit 1
fi

python3 -m pip install -r requirements.txt
python3 main.py $1