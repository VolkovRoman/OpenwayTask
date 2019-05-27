labyrint = [[1,1,1,1,1,1,1,1,1], # 1 - Wall, 0 - Free space
            [1,1,1,1,1,1,1,1,1],
            [1,1,0,0,1,0,0,1,1],
            [1,0,0,0,0,1,0,0,1],
            [1,1,1,1,0,1,0,1,1],
            [1,1,0,0,0,0,0,1,1],
            [1,1,0,1,0,1,0,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1]]
 
def searсh_path(data,x,y,short_path={}, full_path={}, count=0): #data-labyrint; х,у - point where we are
                                                               #short_path - {key=точка куда идём: value=откуда идём}
                                                               #full_path - {key=точка : value=кол-во шагов до точки}
                                                               #count - step count
    full_path[(x,y)] = count # Write enrty point and counting steps to it.
    if x==2 and y ==6: # Exit point
        return full_path, short_path
    walks = [(-1,0),(0, 1),(1, 0),(0, -1)] # Step up, left, down, right,
    for walk_X, walk_Y in walks:
        if data[x + walk_X][y + walk_Y] == 0 and (0<x+walk_X<9 and 0<y+walk_Y<9): # If point is free(0) AND we are inside the labyrint
                                                                                    
            check = full_path.get((x+walk_X,y+walk_Y)) # Looking for that point and counting steps to it.
                                                       # If check=None, we weren't here.
            if check!=None and check>count: # If we were here AND distance to her more than count
                                            
                full_path[(x+walk_X,y+walk_Y)] = count # Overwrite full_path, cause we found a shorter distance.
                short_path[(x + walk_X, y + walk_Y)] = (x, y) # Overwrite short_path, cause we found a point
                                                              # from which this can be reached in short
                searсh_path(data, x + walk_X,y + walk_Y,short_path, full_path,count+1) # Increasing count and run recoursive function
                                                                                      
            else:
                if (x+walk_X,y+walk_Y) not in full_path.keys(): # If at the point where we're going to go have not yet been
                    short_path[(x+walk_X, y+walk_Y)] = (x,y) # write {where going:where we came from}
                    searсh_path(data, x + walk_X, y + walk_Y,short_path, full_path, count + 1) # run recoursing function with count+1
                                                                                              
    return full_path, short_path
 
def short_path(data, path=[], start=(4,2), end=(2,6)): # When we find the exit, here comes short_path from search_path
                                                    # data=short_path, start - entry point, end - exit point
                                                    # path - the path in the form of a list of coordinates
    """Зhere we recursively run from the end point to the start point, restoring the path through the maze"""
    if len(path)==0:
        path.append(end)
    path.append(data[end])
    if data[end]==start:
        return path
    else:
        short_path(data, path, start, data[end])
    return path
 
p = searсh_path(labyrint, 4,2)
if p is None:
    print('No Exit!!!')
else:
    short = short_path(p[1])
    short.reverse()
    for walk in short:
        labyrint[walk[0]][walk[1]] = 3 # There we show the path using number 3
    for see in labyrint:
        print(see)
