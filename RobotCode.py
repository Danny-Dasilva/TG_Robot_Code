# Tank drive code for the google coral
# Author: Danny Dasilva
# License: Public Domain 


from __future__ import division
from app.controller import ControllerInput
from time import sleep
import pygame
import csv
import sys
from adafruit_servokit import ServoKit
import os
# set path to current dir for csv file
path = os.path.dirname(os.path.abspath(__file__))
sleep(1)

os.environ["SDL_VIDEODRIVER"] = "dummy"


#controller Disconnect 
controller = ControllerInput()


# setting 16 channels for hat as well as i2c address to 60
kit = ServoKit(channels=16, address=96)


#Pinout map 
'''
0 left motor
1 right motor
2 left motor 2
3 right motor 2

4 arm motor 1
5 arm motor 2
6 servo 1
7 servo 2test

'''
servo_5 = 0
# Configure min and max servo angle
aservo_min = 0  
aservo_max = 360


#sets deadzone
with open(path +'/var.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        deadzone = (float(row["Deadzone"]))

while True:
    if not controller.hasController():
    # handle disconnect
        print('reconnect')
        kit.continuous_servo[0].throttle = deadzone
        kit.continuous_servo[1].throttle = deadzone
        kit.continuous_servo[2].throttle = deadzone
        kit.continuous_servo[3].throttle = deadzone
        kit.continuous_servo[4].throttle = deadzone
        kit.continuous_servo[5].throttle = deadzone
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
            kit.continuous_servo[4].throttle = 1
            print("armA_forward")
        elif RB == 1:
            kit.continuous_servo[4].throttle = -1
            print("armA_back")
        else:
            kit.continuous_servo[4].throttle = deadzone

        #  Arm B motor
        if LT > .75:
            kit.continuous_servo[5].throttle = 1
            print("armB_forward")
        elif RT > .75:
            kit.continuous_servo[5].throttle = -1
            print("armB_back")
        else:
            kit.continuous_servo[5].throttle = deadzone
        
        

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
            print("condition")
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
                kit.continuous_servo[1].throttle = deadzone
                kit.continuous_servo[3].throttle = deadzone
                kit.continuous_servo[0].throttle = deadzone
                kit.continuous_servo[2].throttle = deadzone
                if Back == 1:
                    with open(path + '/var.csv', mode='w') as csv_file:
                        fieldnames = ['Deadzone']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow({'Deadzone': deadzone})
                    break



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

        

        
    
    








