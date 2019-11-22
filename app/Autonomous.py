# Robot Class
# Author: Danny Dasilva
# License: Public Domain 


from Robot import Controller, Py_Hat, Check_Input

class Autonomous():
    def _init__(self):
        #controller class
        self.controller = Controller()


        # initialize Pi Hat
        self.hat = Py_Hat(address=96)


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

        time.sleep(time)

    def backward(self, value, time, invert=False):
        
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

        time.sleep(time)


 
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

        time.sleep(time)
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

        time.sleep(time)

    def stop(self, time):
        self.hat.motor(0, self.deadzone)
        self.hat.motor(2, self.deadzone)
        self.hat.motor(1, self.deadzone)
        self.hat.motor(3,  self.deadzone)

        time.sleep(time)


