import numpy as np

# Maze definition (0 = free, 1 = wall)
maze = np.array([
    [0,1,0,1,0,1,1,1,0,0,1,0],
    [0,1,0,1,0,0,0,1,0,1,1,0],
    [0,0,0,1,0,1,0,0,0,1,1,0],
    [1,0,1,1,0,1,0,1,0,1,1,0],
    [1,0,0,0,0,1,0,1,0,0,0,0],
    [1,1,1,0,1,1,0,1,1,1,1,1],
    [0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,0]
])

row, cols = maze.shape

# Directions (down, right, up, left)
direction = [(1,0),(0,1),(-1,0),(0,-1)]

def valid(x, y):
    #Check if cell is valid inside maze and not a wall
    return 0 <= x < row and 0 <= y < cols and maze[x][y] != 1

# Example heuristic (Manhattan distance to goal)
def h(cell, goal=(0,11)):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])
