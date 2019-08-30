# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain 
from __future__ import division
import time
from time import sleep
import pygame

from adafruit_servokit import ServoKit
import os
# This is set because normally pygame uses this video drive but the google coral does not support it

os.environ["SDL_VIDEODRIVER"] = "dummy"

# setting 16 channels for hat as well as i2c address to 70
kit = ServoKit(channels=16, address=112)
pygame.init()



# Drivetrain Motors
motor_1 = 0
motor_2 = 0
motor_3 = 0
motor_4 = 0

# Arm Motors
arm_1 = 0
arm_2 = 0



servo_5 = 0
servo_6 = 0



#Pinout map 
'''
0 left motor
1 right motor
2 left motor 2
3 right motor 2

4 arm motor 1
5 arm motor 2
6 servo 1
7 servo 2

'''


# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
aservo_min = 0  
aservo_max = 360


bservo_min = 124  
bservo_max = 494


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
            leftstick = gamepad.get_axis(1)
            rightstick = gamepad.get_axis(3)

            LAservo = gamepad.get_button(0)
            RAservo = gamepad.get_button(1)
            LBLservo = gamepad.get_button(2)
            LBservo = gamepad.get_button(3)


            armA_forward = gamepad.get_button(4)
            armA_back = gamepad.get_button(5)
            armB_forward = gamepad.get_button(6)
            armB_back = gamepad.get_button(7)




            
        else:
            LAservo = 0
            RAservo = 0
            LBLservo = 0
            LBservo = 0


            armA_forward = 0
            armA_back = 0
            armB_forward = 0
            armB_back = 0





        #  Arm motor
        if armA_forward == 1:
            kit.continuous_servo[4].throttle = 1
            print("armA_forward active")
        elif armA_back == 1:
            kit.continuous_servo[4].throttle = -1
            print("armA_back")
        else:
            kit.continuous_servo[4].throttle = 0.05
        


        # one servo
        if LAservo == 1:
            servo_5 = servo_5 + .2
            if servo_5 > aservo_max:
                servo_5 = aservo_max
            kit.servo[6].angle = servo_5
            print("LAservo active")
        elif RAservo == 1:
            servo_5 = servo_5 - .2
            if servo_5 < aservo_min:
                servo_5 = aservo_min
            kit.servo[6].angle = servo_5
            print("RAservo active")



        # Joystick Val
        if  abs(leftstick) > .05:
            kit.continuous_servo[0].throttle = leftstick
            print('leftstick')
        if  abs(leftstick) < .05:
            kit.continuous_servo[0].throttle = 0.05
        if  abs(rightstick) > .05:
            kit.continuous_servo[1].throttle = -rightstick
            print('rightstick')
        if  abs(rightstick) < .05:
              kit.continuous_servo[1].throttle = 0.05

            
        
        








