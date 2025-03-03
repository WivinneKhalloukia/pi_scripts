import time
import wiringpi
import sys

print("Start")
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode (pinSwitch, 1)

while True:
    if (wiringpi.digitalRead(pinSwitch) == 0):
        time.sleep(0.5)
        print("Light")
    else:
        print("Dark")
        time.sleep(0.5)