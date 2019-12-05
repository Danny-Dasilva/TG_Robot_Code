#!/bin/bash


if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
	echo "installing auto code on Coral"
  line="@reboot sudo python3 /home/mendel/TG_Robot_Code/Audio/audio_loop.py"
(crontab -u "mendel" -l; echo "$line" ) | crontab -u "mendel" -


else
  # Install gstreamer
  #sudo apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-good py$

  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
	echo "installing auto code on pi"
    line="@reboot sudo python3 /home/pi/Desktop/TG_Robot_Code/Audio/audio_loop.py"
		(crontab -u "pi" -l; echo "$line" ) | crontab -u "pi" -

  


  fi
fi
