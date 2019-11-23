# Robot Class
# Author: Danny Dasilva
# License: Public Domain 


from .Robot import Controller, Py_Hat, Check_Input
from time import sleep

class Autonomous():
    def __init__(self, hat):
        #controller class
        self.controller = Controller()


        # initialize Pi Hat
        self.hat = hat

        # configure deadzone
        self.deadzone = self.controller.deadzone()

    def forward(self, value, time, invert=False):
        if invert == True:    
            self.hat.motor(0, value)
            self.hat.motor(2, value)
            self.hat.motor(1, -value)
            self.hat.motor(3,  -value)
        else:
            self.hat.motor(0, -value)
            self.hat.motor(2, -value)
            self.hat.motor(1, value)
            self.hat.motor(3,  value)

        sleep(time)

    def backward(self, value, time, invert=False):
        
        if invert == True:    
            self.hat.motor(0, -value)
            self.hat.motor(2, -value)
            self.hat.motor(1, value)
            self.hat.motor(3,  value)
        else:
            self.hat.motor(0, value)
            self.hat.motor(2, value)
            self.hat.motor(1, -value)
            self.hat.motor(3,  -value)

        sleep(time)


 
    def turn_right(self, value, time, invert=False):
        if invert == True:    
            self.hat.motor(0, value)
            self.hat.motor(2, -value)
            self.hat.motor(1, value)
            self.hat.motor(3, -value)
        else:
            self.hat.motor(0, value)
            self.hat.motor(2, -value)
            self.hat.motor(1, value)
            self.hat.motor(3, -value)

        sleep(time)
    def turn_left(self, value, time, invert=False):
        
        if invert == True:
            self.hat.motor(0, -value)
            self.hat.motor(2, value)
            self.hat.motor(1, -value)
            self.hat.motor(3,  value)
        else:
            self.hat.motor(0, -value)
            self.hat.motor(2, value)
            self.hat.motor(1, -value)
            self.hat.motor(3,  value)

        sleep(time)

    def stop(self, time=.3):
        self.hat.motor(0, self.deadzone)
        self.hat.motor(2, self.deadzone)
        self.hat.motor(1, self.deadzone)
        self.hat.motor(3,  self.deadzone)

        sleep(time)


