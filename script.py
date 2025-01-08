import cv2
import numpy as np

# Load the maze image
imagePath = "maze.png" 
mazeImage = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

# Threshold the image to binary (Black and White)
_, binaryMaze = cv2.threshold(mazeImage, 128, 255, cv2.THRESH_BINARY)

# Convert binary image to a 2D array 0 for walls, 1 for paths
mazeArray = (binaryMaze == 255).astype(int)  

startPosition = (192, 0) 
startColor = 128 
startRadius = 5  
cv2.circle(binaryMaze, startPosition, startRadius, startColor, -1)  

endPosition = (210, 407)  
endColor = 128  
endRadius = 5 
cv2.circle(binaryMaze, endPosition, endRadius, endColor, -1) 

# Save the processed binary maze
cv2.imwrite("binaryMazeWithDot.png", binaryMaze)

# Print size of the binary image
print("Binary Maze Size (Height x Width):", binaryMaze.shape)

# Print the maze representation as a 2D array
print("Maze representation as a 2D array:")
print(mazeArray)

# Display the binary image with the dot
cv2.imshow("Binary Maze with Dot", binaryMaze)
cv2.waitKey(0)  
cv2.destroyAllWindows()   