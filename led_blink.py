"""
led_blink.py
Pretend LED blinking (console print).
Uses time.sleep(0.5) to pause for half a second.
Loops a number of times and prints ON/OFF in sequence.
"""

import time

def blink(times=3):
    for i in range(times):
        print("💡 LED ON")
        time.sleep(0.5)
        print("LED OFF")
        time.sleep(0.5)

blink(5)
