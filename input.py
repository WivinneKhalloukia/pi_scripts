import time
import wiringpi
import sys

print("Start")
status = 0
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode (pinLed, 1)
wiringpi.pinMode (pinSwitch, 0)

while True:
    if(wiringpi.digitalRead(pinSwitch) == 0):
        time.sleep(0.3)
        if status == 0:
            print("Button Pressed -> led is on")
            status = 1
        else: status = 0
    else:
        print("Button pressed")
        time.sleep(0.3)
        print("led is " , status)
        wiringpi.digitalWrite (pinLed, status)