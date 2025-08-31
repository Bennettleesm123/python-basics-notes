"""
simple_path.py
Basic shortest path in a grid using BFS (no weights).
Finds the shortest path from the top-left corner (0,0) to the bottom-right (3,3) in a small 4×4 grid. Some squares are blocked by obstacles (marked with 1).
Uses a simple search algorithm BFS = Breadth-First Search.
Starts at (0,0), explores all possible moves step by step.
Keeps track of visited spots so it doesn’t get stuck.
Stops when it reaches the goal, printing the path (list of coordinates).
"""

from collections import deque

grid = [
    [0,0,0,1],
    [0,1,0,0],
    [0,0,0,0],
    [1,0,0,0]
]
start = (0,0)
goal = (3,3)

def bfs(start, goal):
    q = deque([(start,[start])])
    seen = {start}
    while q:
        (x,y), path = q.popleft()
        if (x,y) == goal: return path
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<4 and 0<=ny<4 and grid[nx][ny]==0 and (nx,ny) not in seen:
                q.append(((nx,ny), path+[(nx,ny)]))
                seen.add((nx,ny))
    return None

print("Path:", bfs(start, goal))
