



from app.Robot import Controller, Py_Hat, Check_Input, Autonomous

from time import sleep
import os


def my_custom_autonomous():
    robot = Autonomous()
    # Takes a value and time
    robot.forward(.8, 2)
    robot.backward(1, 1)
    robot.turn_left(.5, 2)
    robot.turn_right(.5, 2)
