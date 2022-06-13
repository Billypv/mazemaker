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
   
    maze = [[{"up":False,"down":False,"left":False,"right":False, "start":False, "goal":False, "on_path": False} for k in range(size) ] for l in range(size)]
            
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
    start_point = (random.randint(0,size - 1),random.randint(0,size - 1))
    end_point = (-1,-1)
    while True:
        end_point = (random.randint(0,size - 1),random.randint(0,size - 1))
        if start_point !=end_point:
            break
    maze[start_point[0]][start_point[1]]["start"] = True
    maze[end_point[0]][end_point[1]]["goal"] = True
    return maze, start_point

def print_maze(maze):
    maze_string = ""
    
    size = len(maze)
    for row in maze:
        for i in range(0,2):
            maze_line = ""
            for tile in row:
                if i ==0:
                    maze_line += "+"
                    if(tile["up"]):
                        maze_line+= " "
                    else:
                        maze_line+="—"
                elif i ==1:
                    if(tile["left"]):
                        maze_line += " "
                    else:
                        maze_line += "|"
                    if tile["start"]:
                        maze_line +="S"
                    elif tile["goal"]:
                        maze_line+="E"
                    elif tile["on_path"]:
                        maze_line += "*"
                    else:
                        maze_line += " "
            maze_string += f"\n{maze_line}+" if (i == 0) else f"\n{maze_line}|"
    maze_string
    maze_string+=(maze_string[0:2*size + 2])
    return maze_string

def path_maze(maze, path, visited):
    if maze [path[-1][0]][path[-1][1]]["goal"]:
        for tile in path:
            maze[tile[0]][tile[1]]["on_path"] =True
        return maze
    if maze[path[-1][0]][path[-1][1]]["up"] and (path[-1][0]-1,path[-1][1]) not in visited:
        path.append((path[-1][0]-1,path[-1][1]))
        visited.add((path[-1][0],path[-1][1]))
        return path_maze(maze,path,visited)
    if maze[path[-1][0]][path[-1][1]]["down"] and (path[-1][0]+1,path[-1][1]) not in visited:
        path.append((path[-1][0]+1,path[-1][1]))
        visited.add((path[-1][0],path[-1][1]))
        return path_maze(maze,path,visited)
    if maze[path[-1][0]][path[-1][1]]["left"] and (path[-1][0],path[-1][1]-1) not in visited:
        path.append((path[-1][0],path[-1][1]-1))
        visited.add((path[-1][0],path[-1][1]))
        return path_maze(maze,path,visited)
    if maze[path[-1][0]][path[-1][1]]["right"] and (path[-1][0],path[-1][1]+1) not in visited:
        path.append((path[-1][0],path[-1][1]+1))
        visited.add((path[-1][0],path[-1][1]))
        return path_maze(maze,path,visited)
    return path_maze(maze,path[0:len(path)-1], visited)

        
            

maze, start_point = create_maze(6)

print(print_maze(path_maze(maze,[start_point],{start_point})))
