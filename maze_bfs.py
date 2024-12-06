import tkinter as tk
from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set()

    while queue:

        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = x + dx, y + dy
            if 0 <= i < rows and 0 <= j < cols and maze[i][j] == 0 and (i, j) not in visited:
                visited.add((i, j))
                queue.append(((i, j), path + [(i, j)]))

    return None

def create_maze():
    return [
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0]
    ]

def draw_maze(canvas, maze, path):
    cell_size = 50
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            color = 'white' if cell == 0 else 'black'
            canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color, outline='black')

        if path:
            for (i, j) in path:
                canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill='blue')

def main():
    maze = create_maze()
    start = (0, 0)
    goal = (5, 3)
    test = bfs(maze, start, goal)
    if test:
        print("Path found:", test)
    else:
        print("No path found")

    root = tk.Tk()
    root.title("Maze Solver")
    canvas = tk.Canvas(root, width=len(maze) * 50 , height=len(maze[0]) * 50)
    canvas.pack()

    draw_maze(canvas, maze, test)

    root.mainloop()


main()