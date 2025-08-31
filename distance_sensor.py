"""
Uses Python’s random.uniform(5.0, 100.0) to generate random decimal numbers.
Rounds the number to 2 decimal places. (5.0,100.0),2 the 2
Prints the reading each time.
distance_sensor.py
Simulate a robot distance sensor returning random values.
"""

import random

def get_distance():
    return round(random.uniform(5.0, 100.0), 2)

for _ in range(5):
    print("Distance reading:", get_distance(), "cm")
