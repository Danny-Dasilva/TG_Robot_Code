# Robot Class
# Author: Danny Dasilva
# License: Public Domain 

import pygame
import time
import os
from time import sleep
import csv

from adafruit_servokit import ServoKit


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



class Controller():
    """
    Controller class
    ...

    Methods
    -------
    gamepad(pin, value)
        controls and sets value of a motor
    
    set_button(pin, button)
        Controlls and sets angle of a servo

    set_axis(pin, axis)
        Controlls and sets angle of a servo

    event_get()
        Controlls and sets angle of a servo

    deadzone()
        Reads from csv file and returns deadzone value

    control_loop(pin, increment, hat)
        Controlls and sets angle of a servo
    
    """
    def __init__(self, js_name='Logitech F310'):
        """
        Initializes the Controller class, sets up pygame to be called in later functions
        ...

        Parameters
        ----------
        js_name : string, optional
            The type of controller you are using 
        """

        pygame.init()
        pygame.joystick.init()
        #Redundancy
        if js_name in ('Logitech F310'):
            self.Joystick = JoystickF310
        
        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()

    def set_button(self, button):
        return self.gamepad.get_button(self.Joystick[button])

    def set_axis(self, axis):
        return self.gamepad.get_axis(self.Joystick[axis])
    
    def event_get(self):
        pygame.event.get()

    def deadzone(self):
        """ Set deadzone variable 

        Reads from a csv file and returns a deadzone
        ...

        """


        with open(path +'/var.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                deadzone = (float(row["Deadzone"]))
            return deadzone




    def control_loop(self, increment, hat):
        """ Control loop to set deadzone variable 

        This function takes two arguments, the amount you increment
        ...


        Parameters
        ----------
        increment : int
            the corresponding pin on the pi-hat

        hat : variable
            input value for the motor (ranges from 1 to -1)

        """

        deadzone = self.deadzone()
        controller = Controller('Logitech F310')

        while True:
            pygame.event.get()
            
            Back = controller.set_button('Back')
            B = controller.set_button('B')
            X = controller.set_button('X')

            if B == 1:
                deadzone = deadzone + increment
            if X == 1:
                deadzone = deadzone - increment

            for i in range(4):
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
        add description here
        ...

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



class Check_Input():
    """
    Classs to deal with controller disconnects
    ...

    Methods
    -------
    has_controller()
        returns true or false based on whether or not a controller is plugged in
    
   
    
    """

  def __init__(self):
     """
    Sets class variables for has_controller function and inits pygame
    ...
    """

    pygame.init()
    pygame.joystick.init()
    self.lastTime = 0
    self.lastActive = 0
    self.gamepad = 0
    self.Recon_timeout = 7
    self.Inactivity = 7

  def has_controller(self):
    """Adafruit Servokit implementation of a motor

    This function takes two arguments a pin and a angle. 
    The pin number corresponds to the one on the pi-hat
    ...
    """

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
          gamepad = pygame.joystick.Joystick(0)
        
          gamepad.init()

    return pygame.joystick.get_count() > 0
    
