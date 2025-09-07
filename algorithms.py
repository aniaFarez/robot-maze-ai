from pyamaze import maze,agent,COLOR
from collections import deque
import numpy as np
from queue import PriorityQueue
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.animation as an 
from matplotlib.widgets import Button


direction=[(1,0),(0,1),(-1,0),(0,-1)]

maze = np.array([[0,1,0,1,0,1,1,1,0,0,1,0],
        [0,1,0,1,0,0,0,1,0,1,1,0],
        [0,0,0,1,0,1,0,0,0,1,1,0],
        [1,0,1,1,0,1,0,1,0,1,1,0],
        [1,0,0,0,0,1,0,1,0,0,0,0],
        [1,1,1,0,1,1,0,1,1,1,1,1],
        [0,0,0,0,1,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0,0,0]
        ]
)

row=8
cols=12

def valid(abs,ads):
    return 0 <= abs < row and 0 <= ads < cols and maze[abs][ads]!=1



def DFS(m,start,goal):
    explored=[start]                     
    frontier=[start]
    parents={start:None}

    while frontier:
        cell=frontier.pop()
        if cell==goal:
            path=[]          
            while cell!=start:
                path.append(cell)
                cell=parents[cell]
            return list(reversed(path+[start])),list(explored)
        
        for d in direction:
                if valid(cell[0]+d[0],cell[1]+d[1]):
                    childCell=(cell[0]+d[0],cell[1]+d[1])
                else:
                     continue
                    
                if childCell in explored:
                    continue

                frontier.append(childCell)
                parents[childCell]=cell

        if cell not in explored:
           explored.append(cell)
    return [],explored


def BFS(m,start,goal):
    frontier=deque()
    frontier.append(start)
    explored=[start]
    parents={start:None}
   

    while frontier:
        cell=frontier.popleft()
        if cell==goal:
            path=[]
            while parents[cell]:
                path.append(cell)
                cell=parents[cell]

            return list(reversed(path+[start])),list(explored)
        else:
            for d in direction:
                if valid(cell[0]+d[0],cell[1]+d[1]):
                    childCell=(cell[0]+d[0],cell[1]+d[1])

                else:
                    continue
                if childCell in explored:
                    continue
                frontier.append(childCell)
                parents[childCell]=cell

        if cell not in explored:
           explored.append(cell)

    return [],explored


he={
    (7,0):8,
    (7,1):7,
    (7,2):6,
    (7,7):7,
    (7,8):7,
    (7,9):7,
    (7,10):6,
    (6,0):7,
    (6,1):6,
    (6,2):7,
    (6,3):6,
    (6,6):6,
    (6,7):7,
    (6,8):7,
    (6,9):7,
    (6,10):7,
    (6,11):6,
    (5,3):6,
    (5,6):7,
    (4,2):6,
    (4,6):6,
    (4,9):2,
    (4,10):1,
    (3,1):5,
    (3,4):6,
    (3,6):4,
    (3,8):3,
    (3,11):1,
    (2,4):6,
    (2,7):3,
    (2,11):1,
    (1,0):13,
    (1,2):10,
    (1,8):4,
    (1,11):1,

    (7, 3): 6,
    (4, 3): 6,
    (4, 1): 6,
    (4, 4): 7,
    (2, 1): 4,
    (2, 0): 12,
    (2, 2): 7,
    (0, 0): 15,
    (0, 2): 18,
    (1, 4): 6,
    (0, 4): 8,
    (1, 5): 6,
    (1, 6): 5,
    (2, 6): 4,
    (7, 6): 8,
    (7, 11): 6,
    (2, 8): 3,
    (0, 8): 5,
    (0, 9): 5,
    (4, 8): 2,
    (4, 11): 1,
    (0, 11): 0
}


def h(cell): 
    return he[cell]
def Astar(m,start,goal):
    g={cell :1 for cell in he}
    g[start]=0
    f={cell :float('inf') for cell in he}

    f[start]=h(start)
    open=PriorityQueue()
    open.put((h(start),start))
    parents={start:None}
    explored=[start]

    while open:
        cell=open.get()[1]
        if cell==goal:
            path=[]
            while parents[cell]:
                path.append(cell)
                cell=parents[cell]
            return list(reversed(path+[start])),explored
        
        for d in direction:
                if valid(cell[0]+d[0],cell[1]+d[1]):
                    childCell=(cell[0]+d[0],cell[1]+d[1])
                else:
                    continue

                Tg=g[childCell]+1
                Tf=Tg+h(childCell)

                if Tf<f[childCell]:
                    g[childCell]=Tg
                    f[childCell]=Tf
                    parents[childCell]=cell
                    explored.append(childCell)
                    open.put((Tf,childCell))
    return [],explored








start=(6,0)
goal=(0,11)

path,explored=BFS(maze,start,goal)


fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xticks(np.arange(0, cols, 1))
ax.set_yticks(np.arange(0, row, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlim(0, cols)
ax.set_ylim(0, row)
ax.set_aspect('equal')





for i in range(row):
    for j in range(cols):
        color = 'black' if maze[i][j] == 1 else 'white'
        ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))


def update(step):
    ax.clear()
    ax.set_xticks(np.arange(0, cols, 1))
    ax.set_yticks(np.arange(0, row, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, cols)
    ax.set_ylim(0, row)
    ax.set_aspect('equal')

    #this piece of code draws the maze
    for i in range(row):
        for j in range(cols):
            color = 'black' if maze[i][j] == 1 else '#470b37'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
    ax.invert_yaxis()
    ax.set_axis_off()

    if step<=len(explored):
        for i in range(step):
            x, y = explored[i]
            ax.add_patch(plt.Rectangle((y,x),1,1, color='red'))

    if step >= len(explored):
       for i in range(len(path)):
            x, y = path[i]
            ax.add_patch(plt.Circle((y + 0.5, x + 0.5), 0.3, color='pink'))
    

ani = an.FuncAnimation(fig,update,frames=len(path)+len(explored), interval=500, repeat=False)
plt.gcf().set_facecolor('#091b26')

ax_btn=plt.axes([0.5,0.04,0.09,0.05])
btn1=Button(ax_btn,'BFS algorithm')





plt.show()