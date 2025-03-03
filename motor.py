#import time, wiringpi and sys
import time
import wiringpi
import sys

def motor(_pin):
   wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin, which turns on the motor
   time.sleep(0.01)                   # Wait for 0.10 seconds
   wiringpi.digitalWrite(_pin, 0)    # Write 0 ( LOW ) to pin, which turns off the motor
   time.sleep(0.01)

print("Start")                        # Print "Start" to the console
pin = 2                               # Assign the value 2 to the variable pin
wiringpi.wiringPiSetup()              # Initialize the wiringpi library
wiringpi.pinMode(pin, 6)
wiringpi.pinMode(pin, 8)
wiringpi.pinMode(pin, 10)
wiringpi.pinMode(pin, 12)
wiringpi.pinMode(pin, 16)

for i in range (0,10):                 # Create a loop that goes 10x
   motor(pin)

print("Done")

