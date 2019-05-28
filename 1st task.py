labyrint = [[1,1,1,1,1,1,1,1,1], # 1 - Wall, 0 - Free space
            [1,1,1,1,1,1,1,1,1],
            [1,1,0,0,1,0,0,1,1],
            [1,0,0,0,0,1,0,0,1],
            [1,1,1,1,0,1,0,1,1],
            [1,1,0,0,0,0,0,1,1],
            [1,1,0,1,0,1,0,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1]]
 
def find_way(data,x,y,short_way={}, full_way={}, step_count=0): #data-labyrint; х,у - point where we are
                                                               #short_way - {key=точка куда идём: value=откуда идём}
                                                               #full_way - {key=точка : value=кол-во шагов до точки}
                                                               #step_count - step step_count
    full_way[(x,y)] = step_count # Write enrty point and step_counting steps to it.
    if x==2 and y ==6: # Exit point
        return full_way, short_way
    steps = [(-1,0),(0, 1),(1, 0),(0, -1)] # Step up, left, down, right,
    for step_X, step_Y in steps:
        if data[x + step_X][y + step_Y] == 0 and (0<x+step_X<9 and 0<y+step_Y<9): # If point is free(0) AND we are inside the labyrint
                                                                                    
            check = full_way.get((x+step_X,y+step_Y)) # Looking for that point and step_counting steps to it.
                                                       # If check=None, we weren't here.
            if check!=None and check>step_count: # If we were here AND distance to her more than step_count
                                            
                full_way[(x+step_X,y+step_Y)] = step_count # Overwrite full_way, cause we found a shorter distance.
                short_way[(x + step_X, y + step_Y)] = (x, y) # Overwrite short_way, cause we found a point
                                                              # from which this can be reached in short
                find_way(data, x + step_X,y + step_Y,short_way, full_way,step_count+1) # Increasing step_count and run recoursive function
                                                                                      
            else:
                if (x+step_X,y+step_Y) not in full_way.keys(): # If at the point where we're going to go have not yet been
                    short_way[(x+step_X, y+step_Y)] = (x,y) # write {where going:where we came from}
                    find_way(data, x + step_X, y + step_Y,short_way, full_way, step_count + 1) # run recoursing function with step_count+1
                                                                                              
    return full_way, short_way
 
def short_way(data, path=[], start=(4,2), end=(2,6)): # When we find the exit, here comes short_way from search_path
                                                    # data=short_way, start - entry point, end - exit point
                                                    # path - the path in the form of a list of coordinates
    """Зhere we recursively run from the end point to the start point, restoring the path through the maze"""
    if len(path)==0:
        path.append(end)
    path.append(data[end])
    if data[end]==start:
        return path
    else:
        short_way(data, path, start, data[end])
    return path
 
p = find_way(labyrint, 4,2)
if p is None:
    print('No Exit!!!')
else:
    short = short_way(p[1])
    short.reverse()
    for walk in short:
        labyrint[walk[0]][walk[1]] = 3 # There we show the path using number 3
    for see in labyrint:
        print(see)
