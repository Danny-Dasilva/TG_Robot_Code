import pygame
import time

INACTIVITY_RECONNECT_TIME = 5
RECONNECT_TIMEOUT = 1

class ControllerInput():
  def __init__(self):
    pygame.joystick.init()
    self.lastTime = 0
    self.lastActive = 0

  def hasController(self):
    now = time.time()
    if now - self.lastActive > INACTIVITY_RECONNECT_TIME and now - self.lastTime > RECONNECT_TIMEOUT:
      self.lastTime = now
      pygame.joystick.quit()
      pygame.joystick.init()

    return pygame.joystick.get_count() > 0



controller = ControllerInput()

# ... game loop
while True:

  
    if not controller.hasController():
    # handle disconnect
        print('reconnect')
    else:
        print("controller connected")
 
