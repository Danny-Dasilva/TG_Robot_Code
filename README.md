# TG-Coral-Robot_Code
Google coral Robot Code with the adafruit servokit library

## Get Started
`git clone https://github.com/Danny-Dasilva/TG-Coral-Robot_Code.git`
 
 path to folder 
 `cd TG-Coral-Robot_Code.git`
 
 if you need to install pygame as well as the servokit library
 
 `sh pygame.sh`
 
 if you need just the servokit library
 
 `sh install.sh`
 
 ## Examples
 
 controller map test
 
 `python3 pygame.py`
 
 servokit test
 
 `sudo python3 simple_test.py`
 
 ## Robot Code
 
 
 `sudo python3 RobotCode.py`
 

Map `below` is for the Adafruit PCA_9685 Hat
This is assuming your Logitech controller is in `D` mode

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

Right Drivetrain A  - Ground
Drivetrain - Left strick and Right stick control respective Left and Right sides
Arm 1      - Motor mapped to Joystick buttons, LB to go forward RB to go back
Arm 2      - Motor mapped to Joystick buttons, LT to go forward RT to go back
Servo 1    - Increments servo on button press, A increases values B decreases values
Servo 2    - Increments servo on button press, A increases values B decreases values
Empty      - Not currently mapped anywhere
```
## Mecanum Drive
 
 
 `sudo python3 Mecanum.py`
 

Map `below` is for the Adafruit PCA_9685 Hat
This is assuming your Logitech controller is in `D` mode

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

Right Drivetrain A  - Ground
Drive    - Motor location for each Mecanum wheel. Left stick controls forward, back 
           and strafe. Right stick controls turning
Arm 1    - Motor mapped to Joystick buttons, LB to go forward RB to go back
Arm 2    - Motor mapped to Joystick buttons, LT to go forward RT to go back
Servo 1  - Increments servo on button press, A increases values B decreases values
Servo 2  - Increments servo on button press, A increases values B decreases values
Empty    - Not currently mapped anywhere


```
