from __future__ import division
import time
import pygame
import math as Math
# Import the PCA9685 module.
from adafruit_servokit import ServoKit


# setting 16 channels for hat as well as i2c address to 70
kit = ServoKit(channels=16, address=112)


pygame.init()

# Drivetrain Motors
motor_1 = 0
motor_2 = 0
motor_3 = 0
motor_4 = 0

# Arm Motors
motor_5 = 0
motor_6 = 0
motor_7 = 0
motor_8 = 0



# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
aservo_min = 124  
aservo_max = 494


bservo_min = 124  
bservo_max = 494



joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

while True:
    
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if joystick_count != 0:
            #axis 0 in this case controls forwards backards and 3 controls turning
            r = Math.hypot(my_joystick.get_axis(1), my_joystick.get_axis(3))
            robotAngle = Math.atan2(my_joystick.get_axis(3), my_joystick.get_axis(1)) - Math.pi / 4
            #below controls strafe
            rightX = my_joystick.get_axis(0)
            v1 = r * Math.cos(robotAngle) + rightX
            v2 = r * Math.sin(robotAngle) - rightX
            v3 = r * Math.sin(robotAngle) + rightX
            v4 = r * Math.cos(robotAngle) - rightX
            motor_1 = (190  * v1 + 318)
            motor_2 = (190  * v2 + 318)
            motor_3 = (190  * v3 + 318)
            motor_4 = (190  * v4 + 318)
    
        else:
            motor_1 = 0
            motor_2 = 0
            motor_3 = 0
            motor_4 = 0
    
        pwm.set_pwm(2, 0, int(motor_1)) # back right
        pwm.set_pwm(3, 0, int(motor_2)) # front left
        pwm.set_pwm(4, 0, int(motor_3)) # back left
        pwm.set_pwm(5, 0, int(motor_4)) # front right
           


      
    
pygame.quit()
