"""
robot_move.py
Tiny simulation: robot moves in a 2D grid with commands.
Start position: [0, 0].
A function move(cmd) takes a command.
If it’s "up", increase y.
If it’s "down", decrease y.
"left" decreases x.
"right" increases x.
After each move, print the new position.
The demo makes the robot move up, up, left, down.
"""

position = [0, 0]  # x, y

def move(cmd):
    if cmd == "up":
        position[1] += 1
    elif cmd == "down":
        position[1] -= 1
    elif cmd == "left":
        position[0] -= 1
    elif cmd == "right":
        position[0] += 1
    print("Moved", cmd, "to", position)

# demo
for c in ["up","up","left","down"]:
    move(c)
