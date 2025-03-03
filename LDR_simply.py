import time
import wiringpi
import sys

print("Start")
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode (pinSwitch, 0)

while True:
    print(wiringpi.digitalRead(pinSwitch))
    if (wiringpi.digitalRead(pinSwitch) == 0):
        time.sleep(0.5)
        print("Light")
    else:
        print("Dark")
        time.sleep(0.5)