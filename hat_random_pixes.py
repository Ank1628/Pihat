#!/usr/bin/env python 

from sense_hat import SenseHat
import time
import random

sense = SenseHat()

n = 10

for i in range (n+1):

    x = random.randint(0, 7)

    y = random.randint(0, 7)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    sense.set_pixel(x, y, (r, g, b))

    time.sleep(1)

    sense.set_pixel(x, y, (0, 0, 0))

sense.clear()



