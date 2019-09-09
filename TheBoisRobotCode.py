import pygame
import time
from BrookAPIFixed.BrooklynClass import Brooklyn
brook = Brooklyn()
pygame.init()
gamepad = pygame.joystick.Joystick(0)
gamepad.init()
while True:
    time.sleep(0.04)
    pygame.event.get()
    leftXstick = gamepad.get_axis(0)
    leftYstick = gamepad.get_axis(1)
    if(abs(leftYstick)>0.05):
        brook.setSpeed(1, leftYstick)
        brook.setSpeed(2, leftYstick)
        brook.setSpeed(3, leftYstick)
        brook.setSpeed(4, leftYstick)
    elif(abs(leftYstick)<0.05):
        brook.setSpeed(1, 0)
        brook.setSpeed(2, 0)
        brook.setSpeed(3, 0)
        brook.setSpeed(4, 0)
    if (abs(leftXstick) > 0.05):
        brook.setSpeed(5, leftXstick)
    elif (abs(leftXstick) < 0.05):
        brook.setSpeed(5, 0)

