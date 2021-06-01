#!/usr/bin/env python3

from autopilot.input import Mouse
import random
import time

print("Enter your screen width: ")
width = int(input()) # 1920
print("Enter your screen height: ")
height = int(input()) # 1080

while True:
    mouse = Mouse.create()
    mouse.move(random.randrange(0, width), random.randrange(0, height))
    #mouse.click()
    time.sleep(5)
