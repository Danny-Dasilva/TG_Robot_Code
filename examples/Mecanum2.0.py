# Mecanum code for the google coral
# Author: Danny Dasilva
# License: Public Domain 














from app.Robot import Controller, Py_Hat, Check_Input
from app.Autonomous import Autonomous

from time import sleep
import os


def my_custom_autonomous():
    auto = Autonomous()
    # Takes a value and time

    auto.forward(.8, 2)
    
    auto.backward(1, 2)
    
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

    disconnect = Check_Input()



    while True:

        if not disconnect.has_controller():
            # handle disconnect
            print('reconnect the controller')
                #loop through all the pins and set them to 0
        for pin in range(4):
            hat.motor(pin, deadzone)

        print('reconnect')
        
       
    else:
        controller.event_get()
        
        # setup controls
        leftstick = controller.set_axis('leftstick') # 1
        rightstick = controller.set_axis('rightstick') # 4
        leftstickx = controller.set_axis('leftstickx') # 0
        
        B = controller.set_button('B')
        X = controller.set_button('X')
        A = controller.set_button('A')
        Y = controller.set_button('Y')
        LB = controller.set_button('LB')
        RB = controller.set_button('RB')
        LT = controller.set_axis('LT')
        RT = controller.set_axis('RT')
        Home = controller.set_button('Home')
        Start = controller.set_button('Start')
        Back = controller.set_button('Back')



        
        #  Arm A motor
        if LB == 1:
            hat.motor(4, 1)
            print("Motor Arm 1 forward")
        elif RB == 1:
            hat.motor(4, -1)
            print("Motor Arm 1 back")
        else:
            hat.motor(4, deadzone)


        #  Arm B motor
        if LT > .75:
            hat.motor(5, 1)
            print("Motor Arm 2 forward")
        elif RT > .75:
            hat.motor(5, -1)
            print("Motor Arm 2 back")
        else:
            hat.motor(5, deadzone)



        # Servo 1
        if LT > .75:
            servo = min(servo + .2, servo_max)
            hat.servo(6, servo)
            print("servo 1 active")
        elif RT > .75:
            servo = max(servo - .2, servo_min)
            hat.servo(6, servo)
            print("servo 1 active")
        

        # Servo 2
        if X == 1:
            servo = min(servo + .2, servo_max)
            hat.servo(7, servo)
            print("servo 2 active")

        
        elif Y == 1:
            servo = max(servo - .2, servo_min)
            hat.servo(7, servo)
            print("servo 2 active")



        
            
        #axis 1 in this case controls forwards backards and 2 controls turning
        r = Math.hypot(leftstick, leftstickx)
        robotAngle = Math.atan2(leftstickx, leftstick) - Math.pi / 4
        # below controls strafe
        rightX = my_joystick.get_axis(0)
        v1 = r * Math.cos(robotAngle) + rightX
        v2 = r * Math.sin(robotAngle) - rightX
        v3 = r * Math.sin(robotAngle) + rightX
        v4 = r * Math.cos(robotAngle) - rightX

        hat.motor(0, v1) # back right
        hat.motor(1, v2)  # front left
        hat.motor(2, v3) # back left
        hat.motor(3, v4) # front right



        # motor_1  back right
        # motor_2  front left
        # motor_3  back left
        # motor_4  front right

        # Set Joystick
        


        # Reset Deadzone
        if Start == Y == Home == 1:
            deadzone = controller.control_loop(.01, hat)
        
        # sleep for smooth loops
        sleep(.02)













