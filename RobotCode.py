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


#controller class
controller = ControllerInput('Logitech F310')


# initialize Pi Hat
hat = Py_Hat(address=96)


# configure deadzone
deadzone = Deadzone()



# Configure min and max servo angle as well  as init
servo_min = 0  
servo_max = 360
servo = 0








while True:
    
    if not controller.hasController():
    # handle disconnect
        print('reconnect the controller')
        #loop through all the pins and set them to 0
        for pin in range(16):
            hat.motor(pin, deadzone)

        print('reconnect')
        
       
    else:
        
        controller.eventGet()
     
        # setup controls
        leftstick = controller.setAxis('leftstick')
        rightstick = controller.setAxis('rightstick')
        
        B = controller.setButton('B')
        X = controller.setButton('X')
        A = controller.setButton('A')
        Y = controller.setButton('Y')
        LB = controller.setButton('LB')
        RB = controller.setButton('RB')
        LT = controller.setAxis('LT')
        RT = controller.setAxis('RT')
        Home = controller.setButton('Home')
        Start = controller.setButton('Start')
        Back = controller.setButton('Back')



        
        #  Arm A motor
        if LB == 1:
            hat.motor(4, 1)
            print("Motor Arm 1 forward")
        elif RB == 1:
            hat.motor(4, -1)
            print("Motor Arm 1 back")
        else:
            hat.motor(4, deadzone)


        #  Arm B motor
        if LT > .75:
            hat.motor(5, 1)
            print("Motor Arm 2 forward")
        elif RT > .75:
            hat.motor(5, -1)
            print("Motor Arm 2 back")
        else:
            hat.motor(5, deadzone)



        # Servo 1
        if A == 1:
            servo = min(servo + .2, servo_max)
            hat.servo(6, servo)
            print("servo 1 active")
        elif B == 1:
            servo = max(servo - .2, servo_min)
            hat.servo(6, servo)
            print("servo 1 active")
        

        # Servo 2
        if X == 1:
            servo = min(servo + .2, servo_max)
            hat.servo(7, servo)
            print("servo 2 active")

        
        elif Y == 1:
            servo = max(servo - .2, servo_min)
            hat.servo(7, servo)
            print("servo 2 active")



        # Reset Deadzone
        if Start == Y == Home == 1:
            deadzone = controller.control_loop(.01)
            
            
        # Set Joystick
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
        
        # sleep for smooth loops
        sleep(.02)
        
    
    








