



from app.Robot import Controller, Py_Hat, Check_Input
from app.Autonomous import Autonomous

from time import sleep
import os


def my_custom_autonomous(hat):
    auto = Autonomous(hat)

    # Takes a value and time

    auto.forward(.8, 2)
    your dumb
    auto.backward(1, 2)
    
    auto.turn_left(.5, 2)
    
    auto.turn_right(.5, 2)

    auto.stop()




def my_custom_teleop():
    #controller class
    controller = Controller()

    # initialize Pi Hat
    hat = Py_Hat(address=96)
    
    while True:
        controller.event_get()
        # setup controls
        leftstick = controller.set_axis('leftstick')
        rightstick = controller.set_axis('rightstick')
        LT = controller.set_axis('LT')

        # Button press to run Autonomous
        if LT > .75:
            my_custom_autonomous(hat) 

        # drivetrain examples
        hat.motor(0, leftstick)
        hat.motor(1, -rightstick)
        # sleep for smooth loops
        sleep(.02)
        










