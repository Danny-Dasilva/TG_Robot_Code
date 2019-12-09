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