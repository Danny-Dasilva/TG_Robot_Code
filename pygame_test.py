
# Simple pygame test for the google coral
# Maps the gamepad for a Logitech controller
# Author: Danny Dasilva
# License: Public Domain 

from __future__ import division
import pygame
from time import sleep
import os
# This is set because normally pygame uses this video drive but the google coral does not support it

os.environ["SDL_VIDEODRIVER"] = "dummy"



pygame.init()

joystick_count = pygame.joystick.get_count()
print(joystick_count)
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print('init')


while True:
    pygame.event.get()
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         done = True   
    # D mode
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
       

    else:
        A = 0
        B = 0
    
    if X == 1:
        print('X pressed')
    if A == 1:
        print('A pressed')
    if B == 1:
        print('B pressed')
    if Y == 1:
        print('Y pressed')

    if LB == 1:
        print('LB pressed')
    if RB == 1:
        print('RB pressed')
    if LT > .7:
        print('LT pressed')
    if RT > .7 :
        print('RT pressed')
    
    if  abs(leftstick) > .05:
        print('leftstick', leftstick)
    if  abs(rightstick) > .05:
        print('rightstick', rightstick)
    sleep(.05)







