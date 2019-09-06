#!/bin/bash

line="@reboot sudo python3 /home/mendel/TG-Coral-Robot_Code/RobotCode.py"
(crontab -u "mendel" -l; echo "$line" ) | crontab -u "mendel" -

