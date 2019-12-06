#!/bin/bash
export XDG_RUNTIME_DIR="/run/user/1000"

while :
do
  mplayer /home/mendel/TG_Robot_Code/Audio/host.mp3
  mplayer /home/mendel/TG_Robot_Code/Audio/ip.mp3
  mplayer /home/mendel/TG_Robot_Code/Audio/status.mp3
done




