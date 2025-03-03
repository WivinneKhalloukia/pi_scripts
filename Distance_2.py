import time
import wiringpi
import sys

print("Start")
pintrig = 1
pinecho = 3
wiringpi.wiringPiSetup()
wiringpi.pinMode(pintrig, 1) #1 is output
wiringpi.pinMode(pinecho,0) #0 is input

print("sending high signal")
wiringpi.digitalWrite(pintrig, 1)
time.sleep(10/1000000.0)
print("sending low signal ")
wiringpi.digitalWrite(pintrig,0)

while (wiringpi.digitalRead(pinecho) == 0):
    print("waiting for echo")
    signalhigh = time.time()
while (wiringpi.digitalRead(pinecho) == 1):
    print("waiting for high echo")
    timepassed = time.time()

timebetween = timepassed - signalhigh
distance = timebetween * 17000
print(distance)
time.sleep(0.5)