# TG_Robot_Code
Robot Code for Tech garage compatible with the Google Coral and Raspberry Pi

## Get Started
`git clone https://github.com/Danny-Dasilva/TG_Robot_Code.git`
 
 path to folder 
 
 `cd TG_Robot_Code`
 
 install dependencies 
 
 `sh scripts/install.sh`
 
 

## Autoboot code

`sh scripts/auto.sh`

This will put the `Robot code.py` path in your crontab which will run on boot

 ## Examples
In `test/`
 
 controller map test
 
 `python3 pygame.py`
 
 Plug in a motor or servo on `pin 1` to test the servokit library
 
 `sudo python3 simple_test.py`
 
 ## Robot Code
 
 
 `sudo python3 RobotCode.py`
 

Map `below` is for the Adafruit PCA_9685 Hat
This is assuming your Logitech controller is in `X` mode

```
Tank Drive

  Left Drivetrain A -> 0   
 Right Drivetrain A -> 1    
  Left Drivetrain B -> 2   
 Right Drivetrain B -> 3  
        Motor Arm 1 -> 4   
        Motor Arm 2 -> 5  
            Servo 1 -> 6  
            Servo 2 -> 7
              Empty -> 8  
              Empty -> 9  
              Empty -> 10
              Empty -> 11 
              Empty -> 12 
              Empty -> 13 
              Empty -> 14  
              Empty -> 15  

Drivetrain - Left stick and Right stick control respective Left and Right sides
Arm 1      - Motor mapped to Joystick buttons, LB to go forward RB to go back
Arm 2      - Motor mapped to Joystick buttons, LT to go forward RT to go back
Servo 1    - Increments servo on button press, A increases values B decreases values
Servo 2    - Increments servo on button press, X increases values Y decreases values
Empty      - Not currently mapped anywhere
```
## Mecanum Drive
 
 
 `sudo python3 Mecanum.py`
 

Map `below` is for the Adafruit PCA_9685 Hat
This is assuming your Logitech controller is in `X` mode

```
Mecanum Drive

   Back Right Drive -> 0   
   Front Left Drive -> 1    
    Back Left Drive -> 2   
  Front Right Drive -> 3  
              Arm 1 -> 4   
              Arm 2 -> 5  
            Servo 1 -> 6  
            Servo 2 -> 7
              Empty -> 8  
              Empty -> 9  
              Empty -> 10
              Empty -> 11 
              Empty -> 12 
              Empty -> 13 
              Empty -> 14  
              Empty -> 15  

Drive    - Motor location for each Mecanum wheel. Left stick controls forward, back 
           and strafe. Right stick controls turning
Arm 1    - Motor mapped to Joystick buttons, LB to go forward RB to go back
Arm 2    - Motor mapped to Joystick buttons, LT to go forward RT to go back
Servo 1  - Increments servo on button press, A increases values B decreases values
Servo 2  - Increments servo on button press, X increases values Y decreases values
Empty    - Not currently mapped anywhere


```

## Troubleshooting

 This library assumes you are mounting on the 0x60 i2c bus
 
 If you are getting an i2c device not found at 60 error you can solder i2c A5 
 
 Or remove the address parameter in the line below 
 
 `hat = Py_Hat(address=96) -> hat = Py_Hat()`


## Autonomous and Custom Telep

 ask for a hat_switch

 **All** custom code goes in the file `My_Custom_Code.py`
 
 there are two classes for custom code

 ```python
def my_custom_autonomous():
```
and 
```python
def my_custom_teleop():
```

Autonomous and teleop code should always go under these functions

### my_custom_autonomous

example

```python
def my_custom_autonomous(hat):
    auto = Autonomous(hat)

    # Takes a value and time
    auto.forward(.8, 2)
    auto.backward(1, 1)
    auto.turn_left(.5, 2)
    auto.turn_right(.5, 2)
    auto.stop()
```


### my_custom_teleop
```python
def my_custom_teleop():
    #controller class
    controller = Controller()

    # initialize Pi Hat
    hat = Py_Hat(address=96)

    # configure deadzone
    deadzone = controller.deadzone()

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
        hat.motor(2, leftstick)
        # sleep for smooth loops
        sleep(.02)
```