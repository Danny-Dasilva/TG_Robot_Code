# Robot Code for Tech Garage
# Author: Danny Dasilva
# License: Public Domain 

from app.Robot import Controller, Py_Hat
from My_Custom_Code import my_custom_teleop
from time import sleep
import os
from time import sleep





#controller class
controller = Controller()


# initialize Pi Hat
hat = Py_Hat(address=96)


change = False

deadzone, custom_code = controller.read()


# Configure min and max servo angle as well  as init
servo_min = 0  
servo_max = 360
servo = 0

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    
    if not controller.has_controller():
    # handle disconnect
        print('reconnect the controller')

        #loop through all the pins and set them to 0
        for pin in range(16):
            hat.motor(pin, deadzone)
        
       
    else:
        controller.event_get()
        
        # setup controls
        leftstick = controller.set_axis('leftstick')
        rightstick = controller.set_axis('rightstick')
        
        B = controller.set_button('B')
        X = controller.set_button('X')
        A = controller.set_button('A')
        Y = controller.set_button('Y')
        LB = controller.set_button('LB')
        RB = controller.set_button('RB')
        LT = controller.set_axis('LT')
        RT = controller.set_axis('RT')
        Home = controller.set_button('Home')
        Start = controller.set_button('Start')
        Back = controller.set_button('Back')


        
        
        #  Arm A motor
        if LB == 1:
            hat.motor(4, 1)
            print("Motor Arm 1 forward")
        elif RB == 1:
            hat.motor(4, -1)
            print("Motor Arm 1 back")
        else:
            hat.motor(4, deadzone)
            
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


        # Reset Deadzone
        if Start == Y == Home == 1:
            deadzone = controller.control_loop(.01, hat)
        
        
     
        if Start == A == Home == 1:
            if change == False:
                
                custom_code = controller.read_and_write(deadzone, change=True)
                change = True
        print(custom_code)
        if i > 50:
            if custom_code == 'True':
                my_custom_teleop()
        #sleep for smooth loops
        
        sleep(.02)
        










