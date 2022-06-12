from hashlib import new
import numpy as np
import matplotlib.pyplot as plt
import random


def frontier_generation(random_node, size,frontier,visited_nodes):
    if(random_node[0] == 0):
        if random_node[1] == 0:
            frontier.add((0,1))
            frontier.add((1,0))
        elif random_node[1] == size -1:
            frontier.add((0,size-2))
            frontier.add((1,size-1))
        else:
            frontier.add((random_node[0],random_node[1]-1))
            frontier.add((random_node[0],random_node[1]+1))
            frontier.add((random_node[0]+1,random_node[1]))
    elif(random_node[0] == size -1):
        if random_node[1] == 0:
            frontier.add((size-2,0))
            frontier.add((size-1,1))
        elif random_node[1] == size -1:
            frontier.add((size-1,size-2))
            frontier.add((size-2,size-1))
        else:
            frontier.add((random_node[0],random_node[1]-1))
            frontier.add((random_node[0],random_node[1]+1))
            frontier.add((random_node[0]-1,random_node[1])) 
    elif(random_node[1] == 0):
            frontier.add((random_node[0]+1,random_node[1]))
            frontier.add((random_node[0],random_node[1]+1))
            frontier.add((random_node[0]-1,random_node[1]))
    elif(random_node[1] == size-1):
            frontier.add((random_node[0]+1,random_node[1]))
            frontier.add((random_node[0],random_node[1]-1))
            frontier.add((random_node[0]-1,random_node[1]))
    else:
        frontier.add((random_node[0]+1,random_node[1]))
        frontier.add((random_node[0],random_node[1]-1))
        frontier.add((random_node[0]-1,random_node[1]))
        frontier.add((random_node[0],random_node[1]+1))
        
    frontier = {tile for tile in frontier if tile not in visited_nodes}
    return frontier     



def create_maze(size):
   
    maze = [[{"up":False,"down":False,"left":False,"right":False} for k in range(size) ] for l in range(size)]
            
    current_node =(random.randint(0,size - 1),random.randint(0,size - 1))
    visited_nodes ={current_node}
    frontier = frontier_generation(current_node,size,set(),visited_nodes)
    while frontier:
        new_node = random.choice(sorted(frontier))
        if (new_node[0]+1, new_node[1]) in visited_nodes:
            maze[new_node[0]][new_node[1]]["down"] = True
            maze[new_node[0]+1][new_node[1]]["up"] = True
        elif (new_node[0]-1, new_node[1]) in visited_nodes:
            maze[new_node[0]][new_node[1]]["up"] = True
            maze[new_node[0]-1][new_node[1]]["down"] = True
        elif (new_node[0], new_node[1]+1) in visited_nodes: 
            maze[new_node[0]][new_node[1]]["right"] = True
            maze[new_node[0]][new_node[1]+1]["left"] = True
        elif (new_node[0], new_node[1]-1) in visited_nodes:
            maze[new_node[0]][new_node[1]]["left"] = True
            maze[new_node[0]][new_node[1]-1]["right"] = True
        visited_nodes.add(new_node)
        frontier.remove(new_node)
        frontier = frontier_generation(new_node,size,frontier,visited_nodes)  
    new_maze = dict();     
    for i in range(size):
        for j in range(size):
            new_maze[(i,j)] = [maze[i][j],""]
       
    print(new_maze)
    return new_maze

def print_maze(maze):
    for i, j in maze:
        walls, _ = maze[i, j]
        if walls['up']:
            plt.plot([i, i+1], [j+1, j+1], 'b-')
        if walls['right']:
            plt.plot([i+1, i+1], [j, j+1], 'b-')
        if walls['down']:
            plt.plot([i, i+1], [j, j], 'b-')
        if walls['left']:
            plt.plot([i, i], [j, j+1], 'b-')
    plt.savefig("please_work.png")



print_maze(create_maze(6))
