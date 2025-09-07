import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

from maze_data import maze, row, cols

def visualize(path, explored):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xticks(np.arange(0, cols, 1))
    ax.set_yticks(np.arange(0, row, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, cols)
    ax.set_ylim(0, row)
    ax.set_aspect('equal')

    def update(step):
        ax.clear()
        ax.set_xticks(np.arange(0, cols, 1))
        ax.set_yticks(np.arange(0, row, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(0, cols)
        ax.set_ylim(0, row)
        ax.set_aspect('equal')

        # Draw maze
        for i in range(row):
            for j in range(cols):
                color = 'black' if maze[i][j] == 1 else '#470b37'
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
        ax.invert_yaxis()
        ax.set_axis_off()

        # Draw explored nodes
        if step <= len(explored):
            for i in range(step):
                x, y = explored[i]
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color='red'))

        # Draw final path
        if step >= len(explored):
            for i in range(len(path)):
                x, y = path[i]
                ax.add_patch(plt.Circle((y + 0.5, x + 0.5), 0.3, color='pink'))

    ani = an.FuncAnimation(fig, update, frames=len(path) + len(explored), interval=500, repeat=False)
    plt.gcf().set_facecolor('#091b26')
    plt.show()
