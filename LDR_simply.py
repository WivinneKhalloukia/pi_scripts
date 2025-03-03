import time
import wiringpi
import sys

print("Start")
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode (pinSwitch, 0)

while True:
    if (wiringpi.digitalRead(pinSwitch) == 0):
        time.sleep(0.5)
        print("Ohno, the sun!")
    else:
        print("It's dark as fuck in here")
        time.sleep(0.5)
