"""
distance_sensor.py
Simulate a robot distance sensor returning random values.
"""

import random

def get_distance():
    return round(random.uniform(5.0, 100.0), 2)

for _ in range(5):
    print("Distance reading:", get_distance(), "cm")
