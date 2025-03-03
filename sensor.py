import time
import wiringpi
import sys

print("Start")
pinSensor = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode (pinSensor, 0)

while True:
    print(wiringpi.digitalRead(pinSensor))
    if(wiringpi.digitalRead(pinSensor) == 0):
        print("Light")
        time.sleep(0.5)

    else:
        print("Dark")
        time.sleep(0.5)

