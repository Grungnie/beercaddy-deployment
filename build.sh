#!/bin/bash

root=$1
echo $root

cd $root

virtualenv -p python3 $root/venv
source $root/venv/bin/activate
pip install -r $root/requirements.txt

arduino --upload $root/arduino/arduino.ino --board arduino:avr:mega --port /dev/ttyACM0 --pref build.path=$root/../arduino-build

exec python $root/main.py
