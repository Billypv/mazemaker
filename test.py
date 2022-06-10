import numpy as np
import random

def createMaze(size):
    maze = [0]
    maze = maze * size ** 2
    randomStart =random.randint(0,size**2 - 1)
    randomEnd = randomStart
    while(randomEnd == randomStart):
        randomEnd = random.randint(0,size**2 - 1)
    t = (randomStart,randomEnd)
    
    maze[t[0]] = 2
    
    
    return maze
    # for location in maze:
        
        

def printMaze(maze):
    size = int(len(maze)**(1/2))
    for i in range(size,len(maze)+size,size):
        print(maze[i-size:i])
        
printMaze(createMaze(6))

    