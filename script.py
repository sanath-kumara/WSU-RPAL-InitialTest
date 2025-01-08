import cv2
import numpy as np
from collections import deque

# Load and process the maze image
ImagePath = "maze.png"
MazeImage = cv2.imread(ImagePath, cv2.IMREAD_GRAYSCALE)
_, BinaryMaze = cv2.threshold(MazeImage, 128, 255, cv2.THRESH_BINARY)
mazeArray = (BinaryMaze == 255).astype(int)  # 1 for paths, 0 for walls

# Define the start and end positions
StartPosition = (5, 192) 
EndPosition = (400, 210) 

# BFS Algorithm
def bfs(maze, start, end):
    rows, cols = maze.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = np.zeros_like(maze)  # To keep track of visited nodes
    queue = deque([(start, [start])])  

    while queue:
        (currentRow, currentCol), path = queue.popleft()

        # Check if robot reached the destination
        if (currentRow, currentCol) == end:
            return path

        # Explore neighbors
        for dr, dc in directions:
            newRow, new_col = currentRow + dr, currentCol + dc

            # Check bounds and if the cell is a path and not visited
            if 0 <= newRow < rows and 0 <= new_col < cols:
                if maze[newRow, new_col] == 1 and not visited[newRow, new_col]:
                    visited[newRow, new_col] = 1
                    queue.append(((newRow, new_col), path + [(newRow, new_col)]))

                    cv2.circle(BinaryMaze, (new_col, newRow), 1, 128, -1)
                    cv2.imshow("Exploring Maze", BinaryMaze)
                    cv2.waitKey(1) 

    return None 

Path = bfs(mazeArray, StartPosition, EndPosition)

if Path:
    for row, col in Path:
        cv2.circle(BinaryMaze, (col, row), 1, (0, 0, 255), -1)
        cv2.imshow("Final Path", BinaryMaze)
        cv2.waitKey(10)  
else:
    print("No path found.")

cv2.waitKey(0)
cv2.destroyAllWindows()  