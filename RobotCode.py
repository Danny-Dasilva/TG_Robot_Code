# Tank drive code for the google coral
# Author: Danny Dasilva
# License: Public Domain 


from __future__ import division
import time
from time import sleep
import pygame

from adafruit_servokit import ServoKit
import os
sleep(3)


# This is set because normally pygame uses this video drive but the google coral does not support it

os.environ["SDL_VIDEODRIVER"] = "dummy"

# setting 16 channels for hat as well as i2c address to 70
kit = ServoKit(channels=16, address=96)

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


deadzone = 0.05

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

print("hello")

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    print("hello")
    gamepad = pygame.joystick.Joystick(0)
    
    gamepad.init()


while True:
        sleep(.01)
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        pygame.event.get()
        #if event.type == pygame.QUIT:
            #done = True
        if joystick_count != 0:
            leftstick = gamepad.get_axis(1)
            rightstick = gamepad.get_axis(4)
            
            B = gamepad.get_button(1)
            X = gamepad.get_button(2)
            A = gamepad.get_button(0)
            Y = gamepad.get_button(3)
            LB = gamepad.get_button(4)
            RB = gamepad.get_button(5)
            LT = gamepad.get_axis(2)
            RT = gamepad.get_axis(5)
            Home = gamepad.get_button(8)
            Start = gamepad.get_button(7)
            Back = gamepad.get_button(6)




            
        else:
            A = 0
            B = 0
            X = 0
            Y = 0


            LB = 0
            RB = 0
            LT = 0
            RT = 0




        
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
        if LT > .75:
            kit.continuous_servo[5].throttle = 1
            print("armB_forward")
        elif RT > .75:
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


        # Deadzone Test
        if Start == Y == Home == 1:
            
            while Back != 1:
                pygame.event.get()
                Back = gamepad.get_button(6)
                B = gamepad.get_button(1)
                X = gamepad.get_button(2)
                sleep(.03)
                
                if B == 1:
                    deadzone = deadzone + .01
                if X == 1:
                    deadzone = deadzone - .01
                kit.continuous_servo[1].throttle = deadzone
                kit.continuous_servo[3].throttle = deadzone
                kit.continuous_servo[0].throttle = deadzone
                kit.continuous_servo[2].throttle = deadzone




           # Joystick Val
        if  abs(leftstick) > .05:
            kit.continuous_servo[0].throttle = leftstick
            kit.continuous_servo[2].throttle = leftstick
            print('leftstick')
        if  abs(leftstick) < .05:
            kit.continuous_servo[0].throttle = deadzone
            kit.continuous_servo[2].throttle = deadzone
        if  abs(rightstick) > .05:
            kit.continuous_servo[1].throttle = -rightstick
            kit.continuous_servo[3].throttle = -rightstick
            print('rightstick')
        if  abs(rightstick) < .05:
              kit.continuous_servo[1].throttle = deadzone
              kit.continuous_servo[3].throttle = deadzone

            

            
        
        








