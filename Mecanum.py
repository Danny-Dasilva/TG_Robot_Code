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




# Arm Motors
arm_1 = 0
arm_2 = 0




# Servos
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
            #axis 1 in this case controls forwards backards and 2 controls turning
            r = Math.hypot(my_joystick.get_axis(1), my_joystick.get_axis(2))
            robotAngle = Math.atan2(my_joystick.get_axis(2), my_joystick.get_axis(1)) - Math.pi / 4
            # below controls strafe
            rightX = my_joystick.get_axis(0)
            v1 = r * Math.cos(robotAngle) + rightX
            v2 = r * Math.sin(robotAngle) - rightX
            v3 = r * Math.sin(robotAngle) + rightX
            v4 = r * Math.cos(robotAngle) - rightX
            
            
            kit.continuous_servo[0].throttle = v1  # back right
            kit.continuous_servo[1].throttle = v2  # front left
            kit.continuous_servo[2].throttle = v3  # back left
            kit.continuous_servo[3].throttle = v4  # front right

            # motor_1  back right
            # motor_2  front left
            # motor_3  back left
            # motor_4  front right




            A = gamepad.get_button(1)
            B = gamepad.get_button(2)
            X = gamepad.get_button(0)
            Y = gamepad.get_button(3)


            LB = gamepad.get_button(4)
            RB = gamepad.get_button(5)
            LT = gamepad.get_button(6)
            RT = gamepad.get_button(7)




            
        else:
            A = 0
            B = 0
            X = 0
            Y = 0


            LB = 0
            RB = 0
            LT = 0
            RT = 0

            v1 = 0
            v2 = 0
            v3 = 0
            v4 = 0





        #  Arm A motor
        if LB == 1:
            kit.continuous_servo[4].throttle = 1
            print("armA_forward")
        elif RB == 1:
            kit.continuous_servo[4].throttle = -1
            print("armA_back")
        else:
            kit.continuous_servo[4].throttle = 0.05

        #  Arm B motor
        if LT == 1:
            kit.continuous_servo[5].throttle = 1
            print("armB_forward")
        elif RT == 1:
            kit.continuous_servo[5].throttle = -1
            print("armB_back")
        else:
            kit.continuous_servo[5].throttle = 0.05
        
        


        # Servo 1
        if A == 1:
            servo_5 = servo_5 + .2
            if servo_5 > aservo_max:
                servo_5 = aservo_max
            kit.servo[6].angle = servo_5
            print("LAservo active")
        elif B == 1:
            servo_5 = servo_5 - .2
            if servo_5 < aservo_min:
                servo_5 = aservo_min
            kit.servo[6].angle = servo_5
            print("RAservo active")
        
         # Servo 2
        if X == 1:
            servo_5 = servo_5 + .2
            if servo_5 > aservo_max:
                servo_5 = aservo_max
            kit.servo[7].angle = servo_5
            print("LBservo active")
        elif Y == 1:
            servo_5 = servo_5 - .2
            if servo_5 < aservo_min:
                servo_5 = aservo_min
            kit.servo[7].angle = servo_5
            print("RBservo active")




            
        
        








