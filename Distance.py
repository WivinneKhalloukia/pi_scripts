import time
import wiringpi
import sys

input = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(input, 1)
wiringpi.pinMode(output, 0)

while True:
    output = 1
    wait = time.sleep(0.10)
    output = 0

    if input == 0:
        wait
    else:
        signal_high = time.time()

    if input == 1:
        wait
    else:
        signal_low = time.time()

    timepassed = signal_low - signal_high
    distance = timepassed * 17000
    print(distance)
    time.sleep(0.5)