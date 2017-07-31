#!/bin/bash

root=$1
echo $root

cd $root

virtualenv -p python3 $root/venv
source $root/venv/bin/activate
pip install -r $root/requirements.txt
exec python $root/main.py
