
if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
  echo "audio backround"
  sudo pip3 install gTTS
  sudo apt-get install mplayer
  sudo apt-get install alsa-utils

  amixer sset 'Master' 50%


  

else
  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
      echo "audio backround"
      sudo pip3 install gTTS
      sudo apt-get install mplayer
      sudo apt-get install alsa-utils

      amixer sset 'Master' 50%
  fi
fi



