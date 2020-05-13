#!/bin/bash
source env/bin/activate
python3 gui/app.py &
python3 server/server.py