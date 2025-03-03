import time
import wiringpi
import sys

print("Start")
pinSwitch = 1
wiringpi.wiringSetup()
wiringpi.pinMode (pinSwitch, 1)

while True:
    if (wiringpi.digitalRead(pinSwitch) == 1):
        time.sleep(0.5)
        print("Dark")
    else:
        print("light")
        time.sleep(0.5)