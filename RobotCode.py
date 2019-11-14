# Robot Code for Tech Garage
# Author: Danny Dasilva
# License: Public Domain 


from __future__ import division
from app.Robot import ControllerInput, Deadzone, control_loop, Py_Hat
from time import sleep
import pygame
import os
sleep(1)

# Fix for pygame on the coral
os.environ["SDL_VIDEODRIVER"] = "dummy"


#handle controller disconnect
controller = ControllerInput()


# initialize Pi Hat
hat = Py_Hat(address=96)


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


servo = 0
# Configure min and max servo angle
servo_min = 0  
servo_max = 360



deadzone = Deadzone()

while True:
    
    if not controller.hasController():
    # handle disconnect
        print('reconnect')
        hat.motor(0, deadzone)
        hat.motor(1, deadzone)
        hat.motor(2, deadzone)
        hat.motor(3, deadzone)
        hat.motor(4, deadzone)
       
    else:
        #print(gamepad.get_name())
        sleep(.01)
        gamepad = pygame.joystick.Joystick(0)
        pygame.event.get()
     

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



        
        #  Arm A motor
        if LB == 1:
            hat.motor(4, 1)
            
            print("armA_forward")
        elif RB == 1:
            hat.motor(4, -1)
            
            print("armA_back")
        else:
            hat.motor(4, deadzone)

        #  Arm B motor
        if LT > .75:
            hat.motor(5, 1)
            print("armB_forward")
        elif RT > .75:
            hat.motor(5, -1)
            print("armB_back")
        else:
            hat.motor(5, deadzone)
        
        

        # Servo 1
        if A == 1:
            servo = servo + .2
            if servo > servo_max:
                servo = servo_max
            hat.servo(6, servo)
            print("LAservo active")
        elif B == 1:
            servo = servo - .2
            if servo < servo_min:
                servo = servo_min
            hat.servo(6, servo)
            print("RAservo active")
        
        # Servo 2
        if X == 1:

            servo = min(servo + .2, servo_max)


            hat.servo(7, servo)
            print("LBservo active")

        
        elif Y == 1:

            servo = max(servo - .2, servo_min)
            
            hat.servo(7, servo)
            print("RBservo active")


        # Deadzone Test
        if Start == Y == Home == 1:
            deadzone = control_loop()
            


        # Joystick Val
        if  abs(leftstick) > .05:
            hat.motor(0, leftstick)
            hat.motor(2, leftstick)
           
            print('leftstick')
        if  abs(leftstick) < .05:
            hat.motor(0, deadzone)
            hat.motor(2, deadzone)
           
        if  abs(rightstick) > .05:
            hat.motor(1, -rightstick)
            hat.motor(3,  -rightstick)
            print('rightstick')
        if  abs(rightstick) < .05:
            hat.motor(1, deadzone)
            hat.motor(3,  deadzone)

        

        
    
    








