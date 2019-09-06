
if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
  echo "Installing Mercurial and pygame"
  sudo apt-get install mercurial -y
  hg clone https://bitbucket.org/pygame/pygame
  cd pygame
  echo "Installing pygame dependencies"
  sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev \
  libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
  libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev -y
  python3 setup.py build
  sudo python3 setup.py install
  cd ..
  sudo rm -rf pygame
  echo "Installing Servokit"
  sudo pip3 install adafruit-circuitpython-servokit
  echo "Adding Libgiod Bindings"
  wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/libgpiod.sh
  chmod +x libgpiod.sh
  ./libgpiod.sh
  rm -rf ./libgpiod.sh

else
  # Install gstreamer
  sudo apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-good py$

  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
    echo "Installing Raspberry Pi specific dependencies"
    sudo apt-get install python3-rpi.gpio
    # Add v4l2 video module to kernel
    if ! grep -q "bcm2835-v4l2" /etc/modules; then
      echo bcm2835-v4l2 | sudo tee -a /etc/modules
    fi
    sudo modprobe bcm2835-v4l2
  fi
fi



