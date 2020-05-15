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

## Select the proper locale/timezone for your country
This is used to display the date in your own language. In my case for Spain I selected _**es_ES.UTF-8**_ and _**Europe/Madrid**_

```bash
sudo dpkg-reconfigure locales
sudo timedatectl set-timezone Europe/Madrid
```

## Software installation
A fresh copy of Rasbpian Lite is prefered.
```bash
sudo apt install freeglut3-dev
git clone https://github.com/hkfuertes/rpi_display
cd rpi_display
pip3 install -r requirements.txt
cp -r otfs /home/pi/.fonts
```

To create a desktop entry:
```bash
./create.desktop.sh
cp Clock.desktop /home/pi/Desktop
```
Now you need to edit the configuration file, to do so, copy the file `config.yml.template` to `config.yml` and edit it acordingly:

```yaml
owm:
  api_key: <openweathermap_api_key>
  language: es
city: Madrid
country: ES
locale: es_ES.UTF-8
date:
  format: '%A %d de %B'
```

For autorun on startup:
```bash
mkdir -p /home/pi/.config/lxsession/LXDE-pi/
echo "@cd $(pwd) && ./start.sh" >> /home/pi/.config/lxsession/LXDE-pi/autostart
```

### Information
When running a `current.pid`  file is created with the running pid. If you need to kill it you can do:
 ```bash
 cd path/to/rpi_display/folder
kill -9 $(cat current.pid)
```

## TODO
- Disable DPMS/blank screensaver
- Weahter forecast (free?)
- Control brightness with python