import BrooklynAPI.brooklyn as brd
import time
import random
test = brd.Brooklyn("/dev/ttyACM0")
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

motors = [test.getmotor(1,1),test.getmotor(1,2),test.getmotor(2,1),test.getmotor(2,2),test.getmotor(3,1),test.getmotor(3,2),test.getmotor(4,1),test.getmotor(4,2)]


def driveMotors(val):
    for i in motors:
        i.setPWM(val)

def driveMotorsTurn(val):
    motors[0].setPWM(val)
    motors[1].setPWM(val)
    motors[4].setPWM(val)
    motors[5].setPWM(val)
    motors[2].setPWM(-val)
    motors[3].setPWM(-val)
    motors[6].setPWM(-val)
    motors[7].setPWM(-val)

driveMotors(255)
time.sleep(2)
driveMotors(0)
test.end()