# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain 
from __future__ import division
import time
from time import sleep
import pygame
# Import the PCA9685 module.
from adafruit_servokit import ServoKit

pygame.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()


while True:

    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        pygame.event.get()
        #if event.type == pygame.QUIT:
            #done = True
        if joystick_count != 0:


            val = gamepad.get_button(0)
            val_2 = gamepad.get_button(1)
            





            
        else:
            print('no joysticks')
           





        #  Arm motor
        if val == 1:
            
            print("armA_forward active")
        elif val_2 == 1:
            print("armA_back")
        else:
            print('no val')
        


        
        








