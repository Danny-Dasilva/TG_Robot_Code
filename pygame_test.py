
from __future__ import division
import time
from time import sleep
import pygame

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
        pygame.event.get()
       
        








