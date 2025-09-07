from algorithms import BFS, DFS, Astar
from maze_data import maze
from visualization import visualize

if __name__ == "__main__":
    start = (6,0)
    goal = (0,11)

    # Choose algorithm: BFS, DFS, or Astar
    #path, explored = BFS(start, goal)
    path, explored = DFS(start, goal)
    # path, explored = Astar(start, goal)

    visualize(path, explored)
