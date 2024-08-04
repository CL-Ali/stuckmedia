#!/bin/bash

echo "BUILD START"

# Install pip if it's not available
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.9 get-pip.py
    rm get-pip.py
fi

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
