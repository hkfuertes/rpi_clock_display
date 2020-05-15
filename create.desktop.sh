#!/bin/bash

echo "[Desktop Entry]" > Clock.desktop
echo "Version=1.0" >> Clock.desktop
echo "Encoding=UTF-8" >> Clock.desktop
echo "Terminal=false" >> Clock.desktop
echo "Name=Clock" >>Clock.desktop
echo "Exec=$(which python3) $(pwd)/app.py" >> Clock.desktop
echo "Type=Application" >>Clock.desktop
