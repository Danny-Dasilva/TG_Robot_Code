
if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
  echo "audio backround"
  pip3 install pip install gTTS
  sudo apt-get install mplayer
  sudo apt-get install alsa-utils

  amixer sset 'Master' 50%


  

else
  # Install gstreamer
  sudo apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-good py$

  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
      echo "audio backround"
      pip3 install pip install gTTS
      sudo apt-get install mplayer
      sudo apt-get install alsa-utils

      amixer -D pulse sset Master 50%
  fi
fi



