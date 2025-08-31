"""
led_blink.py
Pretend LED blinking (console print).
"""

import time

def blink(times=3):
    for i in range(times):
        print("💡 LED ON")
        time.sleep(0.5)
        print("LED OFF")
        time.sleep(0.5)

blink(5)
