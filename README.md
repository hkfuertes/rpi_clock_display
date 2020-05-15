# Raspberry Pi Clock
This project is a simple Raspberry Pi clock app with wheather and IP information.

![image](pictures/screenshot.jpg "Running")

## Installation
A fresh copy of Rasbpian Lite is prefered.
```bash
sudo apt install freeglut3-dev
pip3 install -r requirements.txt
./create.desktop.sh
cp Clock.desktop /home/pi/Desktop
```
For auto run on startup:
```bash
mkdir -p /home/pi/.config/lxsession/LXDE-pi/
echo "@$(pwd)/app.py" >> /home/pi/.config/lxsession/LXDE-pi/autostart
```


## TODO
- Read config.yml
  - Export OWM key to config.yml
- Weahter forecast (free?)