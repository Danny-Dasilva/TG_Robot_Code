
if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
  echo "Installing Servokit"
  sudo pip3 install adafruit-circuitpython-servokit
  echo "Adding Libgiod Bindings"
  wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/libgpiod.sh
  chmod +x libgpiod.sh
  ./libgpiod.sh
  rm -rf ./libgpiod.sh

else
  # Install gstreamer
  #sudo apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-good py$

  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
    echo "Installing Raspberry Pi specific dependencies"
    
  echo "Installing Servokit"
  sudo pip3 install adafruit-circuitpython-servokit
  echo "Adding Libgiod Bindings"
  wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/libgpiod.sh
  chmod +x libgpiod.sh
  ./libgpiod.sh
  rm -rf ./libgpiod.sh
	sudo pip3 install pygame


  fi
fi



