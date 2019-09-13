import pygame
import time
from BrookAPIFixed.BrooklynClass import Brooklyn
brook = Brooklyn()
pygame.init()
gamepad = pygame.joystick.Joystick(0)
gamepad.init()
try:
    while True:
        time.sleep(0.04)
        pygame.event.get()
        leftXstick = gamepad.get_axis(0)
        rightXstick = gamepad.get_axis(3)
        leftYstick = gamepad.get_axis(1)
        print("LeftXstick", leftXstick)
        print("LeftYstick", leftYstick)
        print("RightXstick", rightXstick)
        if(abs(leftYstick)>0.05):
            brook.setSpeed(1, leftYstick)
            brook.setSpeed(2, leftYstick)
            brook.setSpeed(3, leftYstick)
            brook.setSpeed(4, leftYstick)
        elif(abs(rightXstick)>0.05):
            brook.setSpeed(1, -rightXstick)
            brook.setSpeed(2, -rightXstick)
            brook.setSpeed(3, rightXstick)
            brook.setSpeed(4, rightXstick)
        else:
            brook.setSpeed(1, 0)
            brook.setSpeed(2, 0)
            brook.setSpeed(3, 0)
            brook.setSpeed(4, 0)
        if (abs(leftXstick) > 0.05):
            brook.setSpeed(5, leftXstick)
        elif (abs(leftXstick) < 0.05):
            brook.setSpeed(5, 0)
except (KeyboardInterrupt, SystemExit):
    brook.close()

