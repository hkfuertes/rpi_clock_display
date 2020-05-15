#!/bin/bash
echo "#!/bin/bash" > clock.start.sh
echo "export DISPLAY=:0" >> clock.start.sh
echo "xset s off -dpms" >> clock.start.sh
echo "$(which python3) $(pwd)/app.py" >> clock.start.sh

chmod u+x clock.start.sh

# SH starter script
mv clock.start.sh /home/pi/clock.start.sh

# Autostart
mkdir -p /home/pi/.config/lxsession/LXDE-pi/
echo "@/home/pi/clock.start.sh" >> /home/pi/.config/lxsession/LXDE-pi/autostart