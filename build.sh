#!/bin/bash

root=$1

virtualenv -p python3 $root/venv
source $root/venv/bin/activate
pip install -r $root/requirements.txt
python $root/main.py
