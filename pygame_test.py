
from __future__ import division
import time
from time import sleep
import pygame
import os

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
    
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if joystick_count != 0:
            A = gamepad.get_button(0)
            B = gamepad.get_button(1)
    
        else:
            A = 0
            B = 0
    
        if A == 1:
            print('A pressed')
        if B == 1:
            print('B pressed')
        








