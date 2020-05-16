#!/bin/bash
if [ ! -d "env" ]; then
  python3 -m virtualenv env
  source env/bin/activate
  pip3 install -r requirements.txt
fi
source env/bin/activate
python3 app.py