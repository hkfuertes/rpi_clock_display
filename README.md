# Raspberry Pi Clock
This project is a simple Raspberry Pi clock app with wheather and IP information.

![image](pictures/screenshot.jpg "Running")

## LCD Panel installation
Please refer to your lcd installation process for more detail. For my panel to work I needed to follow this steps on a fresh Raspbian Lite (buster) image:

```bash
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./MHS35-show [orientation]
```
_In my case the orientation that works is 180º_

> Go to lcdwiki for more information: https://github.com/lcdwiki/LCD-show

## Select the proper locale for your country
This is used to display the date in your own language. In my case for Spain I selected _**es_ES.UTF-8**_

```bash
sudo dpkg-reconfigure locales
```

### Disable blanking the screen on Raspbian
To disable screen blanking in raspbian run:

```bash
mkdir -p /home/pi/.config/lxsession/LXDE-pi/
echo "@xset s noblank" >> ~/.config/lxsession/LXDE-pi/autostart
echo "@xset s off" >> ~/.config/lxsession/LXDE-pi/autostart
echo "@xset -dpms" >> ~/.config/lxsession/LXDE-pi/autostart
```

> Command `mkdir -p /home/pi/.config/lxsession/LXDE-pi/` makes sure that the forlder exist. we will be executing it everytime just in case.

## Software installation
A fresh copy of Rasbpian Lite is prefered.
```bash
sudo timedatectl set-timezone Europe/Madrid
sudo apt install freeglut3-dev
git clone https://github.com/hkfuertes/rpi_display
cd rpi_display
pip3 install -r requirements.txt
./create.desktop.sh
cp Clock.desktop /home/pi/Desktop
```
For auto run on startup:
```bash
mkdir -p /home/pi/.config/lxsession/LXDE-pi/
echo "@$(pwd)/app.py" >> /home/pi/.config/lxsession/LXDE-pi/autostart
```

### Information
When running a `current.pid`  file is created with the running pid. If you need to kill it you can do:
 ```bash
kill -9 $(cat path/to/rpi_display/folder/current.pid)
```

## TODO
- Weahter forecast (free?)
- Disable screensaver
- Control brightness with python