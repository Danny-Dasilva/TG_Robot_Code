



from app.Robot import Controller, Py_Hat, Check_Input
from app.Autonomous import Autonomous

from time import sleep
import os


def my_custom_autonomous():
    auto = Autonomous()
    # Takes a value and time

    auto.forward(.8, 2)
    
    auto.backward(1, 1)
    
    auto.turn_left(.5, 2)
    
    auto.turn_right(.5, 2)

    auto.stop()




def my_custom_teleop():

    #controller class
    controller = Controller()

    # initialize Pi Hat
    hat = Py_Hat(address=96)

    # configure deadzone
    deadzone = controller.deadzone()

    # Configure min and max servo angle as well  as init
    servo_min = 0  
    servo_max = 360
    servo = 0

    while True:

        controller.event_get()
            
        # setup controls
        leftstick = controller.set_axis('leftstick')
        rightstick = controller.set_axis('rightstick')
        
        B = controller.set_button('B')
        A = controller.set_button('A')
        LT = controller.set_axis('LT')

        # Button press to run Autonomous
        if LT > .75:
            my_custom_autonomous()

      
        # Servo example
        if A == 1:
            servo = min(servo + .2, servo_max)
            hat.servo(6, servo)
            print("servo 1 active")
        elif B == 1:
            servo = max(servo - .2, servo_min)
            hat.servo(6, servo)
            print("servo 1 active")
            
        
        # drivetrain examples
        hat.motor(0, leftstick)
        hat.motor(2, leftstick)
            
        hat.motor(1, -rightstick)
        hat.motor(3,  -rightstick)

        
        # sleep for smooth loops
        sleep(.02)
        










