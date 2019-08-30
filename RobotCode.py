# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain 
from __future__ import division
import time
from time import sleep
import pygame
import Adafruit_PCA9685
sleep(10)
pygame.init()


# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
motor_1 = 0
motor_2 = 0
motor_3 = 0
motor_4 = 300
# Configure min and max servo pulse lengths
servo_min = 200
servo_max = 494


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')

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
            rightstick = gamepad.get_axis(4)
            Lservo = gamepad.get_button(0)
            Rservo = gamepad.get_button(1)
            Lservo2 = gamepad.get_button(2)
            Rservo2 = gamepad.get_button(3)
        else:
            leftstick = 0
            rightstick = 0
            Lservo = 0
            Rservo = 0
            Lservo2 = 0
            Rservo2 = 0
        if Lservo2 == 1:
            motor_4 = motor_4 + .3
            if motor_4 > servo_max:
                motor_4 = servo_max
            print("Lservo active")
        elif Rservo2 == 1:
            motor_4 = motor_4 - .3
            if motor_4 < servo_min:
                motor_4 = servo_min
            print("Rservo active")
            
        if Lservo == 1:
            motor_3 = (185 * Lservo +380)
            
            print("Lservo active")
        elif Rservo == 1:
            motor_3 = (185 * -Rservo +380)
            
            print("Rservo active")
        else:
            motor_3 = 0
        
        #if motor_3 > 359:
            #motor_3 = 0
        #elif motor_3 < 0:
            #motor_3 = 359
        if  abs(leftstick) > .05:
            motor_1 = (185 * leftstick + 385)
            print('left code running')
        if  abs(leftstick) < .05:
            motor_1 = 0
            print('left not running')
        if  abs(rightstick) > .05:
            motor_2 = (185 * -rightstick + 385)
            print('right code running')
        if  abs(rightstick) < .05:
            motor_2 = 0
            print('right not running')
            
        
        
        
        
        
        print("Motor_3: ", motor_3)
        pwm.set_pwm(0, 0, int(motor_1))
        pwm.set_pwm(1,0, int(motor_2))
        pwm.set_pwm(2, 0, int(motor_3))
        pwm.set_pwm(3, 0, int(motor_4))
 


#pygame.quit()







