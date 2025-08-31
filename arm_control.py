"""
arm_control.py
Simple functions to move a pretend robotic arm.
"""

def pick_up(item):
    print("🤖 Arm picking up", item)

def move_to(x, y):
    print(f"Arm moving to ({x},{y})")

def release():
    print("Arm releasing item")

# demo
pick_up("block")
move_to(3, 4)
release()
