import cv2
import numpy as np
from collections import deque

# Load and process the maze image
ImagePath = "maze.png"
MazeImage = cv2.imread(ImagePath, cv2.IMREAD_GRAYSCALE)
_, BinaryMaze = cv2.threshold(MazeImage, 128, 255, cv2.THRESH_BINARY)
MazeArra = (BinaryMaze == 255).astype(int)  # 1 for paths, 0 for walls

StartPosition = (5, 192)
EndPosition = (400, 210)

# BFS Algorithm
def bfsAlgorithem(maze, start, end):
    rows, cols = maze.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = np.zeros_like(maze)  # To keep track of visited nodes
    queue = deque([start])  # Queue only stores coordinates
    parent = {}  # Dictionary to reconstruct path

    visited[start] = 1

    while queue:
        currentRow, currentCol = queue.popleft()

        # Check if destination is reached
        if (currentRow, currentCol) == end:
            path = []
            while (currentRow, currentCol) in parent:
                path.append((currentRow, currentCol))
                currentRow, currentCol = parent[(currentRow, currentCol)]
            path.reverse()
            return path

        # Explore neighbors
        for dr, dc in directions:
            newRow, newCol = currentRow + dr, currentCol + dc

            # Check bounds and if the cell is a path and not visited
            if 0 <= newRow < rows and 0 <= newCol < cols:
                if maze[newRow, newCol] == 1 and not visited[newRow, newCol]:
                    visited[newRow, newCol] = 1
                    parent[(newRow, newCol)] = (currentRow, currentCol)
                    queue.append((newRow, newCol))
    return None

# Find the path using BFS
Path = bfsAlgorithem(MazeArra, StartPosition, EndPosition)

if Path:
    # Draw final path
    for row, col in Path:
        cv2.circle(BinaryMaze, (col, row), 1, (0, 0, 255), -1)
        cv2.imshow("Final Path", BinaryMaze)
        cv2.waitKey(1)
    cv2.waitKey(0)
else:
    print("No path found.")

