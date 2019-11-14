import pygame
import time
import os
from time import sleep
import csv
from adafruit_servokit import ServoKit



path = os.path.dirname(os.path.abspath(__file__))
def Deadzone():

    with open(path +'/var.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            deadzone = (float(row["Deadzone"]))
        return deadzone



def control_loop():
    deadzone = Deadzone()
    gamepad = pygame.joystick.Joystick(0)
    hat = Py_Hat()
    while True:
        pygame.event.get()
        
        Back = gamepad.get_button(6)
        B = gamepad.get_button(1)
        X = gamepad.get_button(2)

        print(Back)
        sleep(.03)
        
        if B == 1:
            deadzone = deadzone + .01
        if X == 1:
            deadzone = deadzone - .01
        for i in range(4):
            hat.motor(i, deadzone)
      

        if Back == 1:
            with open(path + '/var.csv', mode='w') as csv_file:
                fieldnames = ['Deadzone']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Deadzone': deadzone})
            return deadzone


class ControllerInput():
  def __init__(self):
    pygame.init()
    pygame.joystick.init()
    self.lastTime = 0
    self.lastActive = 0
    self.gamepad = 0
    self.Recon_timeout = 7
    self.Inactivity = 7

  def hasController(self):
    now = time.time()
    if now - self.lastActive > self.Inactivity and now - self.lastTime > self.Recon_timeout:
      self.lastTime = now
      pygame.joystick.quit()
      pygame.joystick.init()
    
      joystick_count = pygame.joystick.get_count()
      if joystick_count == 0:
          # No joysticks!
          self.Recon_timeout = 1
          print("Error, I didn't find any joysticks.")
      else:
          
          # Use joystick #0 and initialize it
          gamepad = pygame.joystick.Joystick(0)
        
          gamepad.init()

    return pygame.joystick.get_count() > 0
    
class Py_Hat():
    def __init__(self):
        channels = 16
        address = 96
        kit = ServoKit(channels=channels, address=address)
        self.kit = kit
    def motor(self, pin, value):
        self.kit.continuous_servo[pin].throttle = value
    def servo(self, pin, angle):
        self.kit.servo[pin].angle = angle