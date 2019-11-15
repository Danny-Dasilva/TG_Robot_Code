import pygame
import time
import os
from time import sleep
import csv
#from adafruit_servokit import ServoKit

JoystickF310 = {
		"leftstick" : 1,
		"rightstick" : 4,
		"B" : 1,
		"X" : 2,
		"A" : 0,
		"Y" : 3,
        "LB" : 4,
		"RB" : 5,
		"LT" : 2,
		"RT" : 5,
		"Home" : 8,
		"Start" : 7,
        "Back" : 6,
		
	}


path = os.path.dirname(os.path.abspath(__file__))






class ControllerInput():
    """
    Controller disconnect class for pygame
    ...

    Methods
    -------
    hasController()
        checks if a current controller exists
    
    """
    def __init__(self, js_name):
        pygame.init()
        pygame.joystick.init()
        
        self.lastTime = 0
        self.lastActive = 0
        self.gamepad = 0
        self.Recon_timeout = 7
        self.Inactivity = 7
        #Redundancy
        self.gamepad = pygame.joystick.Joystick(0)
        if js_name in ('Logitech F310'):
            self.Joystick = JoystickF310

    def hasController(self):
        now = time.time()
        if now - self.lastActive > self.Inactivity and now - self.lastTime > self.Recon_timeout:
            self.lastTime = now
        pygame.joystick.quit()
        pygame.joystick.init()
        
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            # No joysticks!
            self.Recon_timeout = 1
            print("Error, I didn't find any joysticks.")
        else:
            
            # Use joystick #0 and initialize it

            #Redundancy
            self.gamepad = pygame.joystick.Joystick(0)
            
            gamepad.init()

        return pygame.joystick.get_count() > 0




    def Gamepad(self):
        gamepad = pygame.joystick.Joystick(0)

        return gamepad


    def setButton(self, button):
       
        return self.gamepad.get_button(self.Joystick[button])

    def setAxis(self, axis):
        return self.gamepad.get_axis(self.Joystick[axis])
    def eventGet(self):
        return pygame.event.get()



    
    def Deadzone(self):

        with open(path +'/var.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.deadzone = (float(row["Deadzone"]))
            return deadzone




    def control_loop(self):
        deadzone = Deadzone()
        controller = ControllerInput('Logitech F310')
        hat = Py_Hat()
        while True:
            pygame.event.get()
            
            Back = controller.setButton('Back')
            B = controller.setButton('B')
            X = controller.setButton('X')

        
            
            
            if B == 1:
                deadzone = deadzone + .01
            if X == 1:
                deadzone = deadzone - .01

            for i in range(16):
                hat.motor(i, deadzone)
        

            if Back == 1:
                with open(path + '/var.csv', mode='w') as csv_file:
                    fieldnames = ['Deadzone']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({'Deadzone': deadzone})
                return deadzone
            sleep(.03)




class Py_Hat():
    """
    Py-Hat class for the Adafruit_PCA1986 hat
    ...

    Methods
    -------
    motor(pin, value)
        controls and sets value of a motor
    
    servo(pin, angle)
        Controlls and sets angle of a servo
    
    """
    
    def __init__(self, channels = 16, address = 64):
        """

        Parameters
        ----------
        channels : int, optional
            Number of pins on the hat
        address : int, optional
            hex adress for i2c bus (default is 0x40)
        """
        
        
        kit = ServoKit(channels=channels, address=address)
        self.kit = kit
        
    def motor(self, pin, value):
        """Adafruit Servokit implementation of a motor

        This function takes two arguments a pin and a value ranging from 1 to -1. 
        The pin number corresponds to the one on the pi-hat
        ...


        Parameters
        ----------
        pin : int
            the corresponding pin on the pi-hat

        value : int
            input value for the motor (ranges from 1 to -1)

        """
        self.kit.continuous_servo[pin].throttle = value
    def servo(self, pin, angle):
        """Adafruit Servokit implementation of a motor

        This function takes two arguments a pin and a angle. 
        The pin number corresponds to the one on the pi-hat
        ...

        Parameters
        ----------
        pin : int
            the corresponding pin on the pi-hat

        angle : int
            set angle of the servo, max angle depends on the type servo
        """
        self.kit.servo[pin].angle = angle

