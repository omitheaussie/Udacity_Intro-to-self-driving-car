import math
import copy
from helpers import Map, load_map, show_map
M=0
goal=0
start=0
explored=[]
frontier=[]

def shortest_path(Mlocal,start_local,goal_local):
    #Initiate global variables
    setglobalmap(Mlocal,goal_local,start_local)
    
    # Initiate path, frontier and first set of node expansion
    path={'1': [start]}
    # Path structure is Path={'1':[n1,n2,....nn, pathcost], '2':[.....], .....}
    path['1'].append(findmincost(path['1']))  
    # Result or the last node on the path is the second to last item in the dictionary value (which is a list)
    result=[path['1'][-2]]   
    # As we are expanding the first node, it is the frontier
    frontier=[path['1'][-2]] 
    roadstosend=M.roads[path['1'][-2]] #This is a list of nodes connected to node1 - these will be frontier after paths are added
    
    # This while loop runs untill the path list returns a path that reaches the goal AND is also the least value path
    # OR it checks for a condition where the least value path in the path list hits a deadend (no connecting nodes)
    # and then it checks the current path list for paths that lead to the goal and returns the result as the one 
    # with minimum path cost.
    
    while not(pathfoundandmincost(path,goal)):
        #rint("Path:", path)
        #print(" ")
        ex=str(whattoexpandnext(path))      # Find the least value path from the path list that will be expanded
        
        # This is the condition where the least value path has hit a deadend and is not a goal
        if ex=='0':
            sendpath=copy.deepcopy(path)
            result=returnleastvaluepath(sendpath,path)
            return result
        
        # Append the current expansion node to explored list
        if path[ex][-2] not in explored:
            explored.append(path[ex][-2])
            
        # Finding roads to send, only send the roads that are not already in the explored list
        b3=[val for val in explored if val in M.roads[path[ex][-2]]]
        roadstosend=copy.deepcopy(M.roads[path[ex][-2]])
        for val in b3:
            if val in roadstosend:
                roadstosend.remove(val)
        
        # Add the roads to which ex node will reach to frontier
        if len(roadstosend)>0:
            for r in roadstosend:
                if r not in explored:
                    if r not in frontier:
                        frontier.append(r)
            # Remove the ex node from the frontier.
            frontier.remove(path[ex][len(path[ex])-2])
            # Expand the current path (ex) with the roads which are not in the explored list (roadstosend)
            path=expandedpath(path,roadstosend,ex)
        else:  
            # if the roadstosend list returns 0, that means the connected nodes are already in the explored list or has no connections.
            # so no point in keeping that path in the path list.
            path.pop(ex,None)
        #show_map(M, start, goal, path[ex][0:-2])
        
        
    # This is where the while loop above has returned without a result, meaning it has found a path that leads to the goal and 
    # also is the least path cost
    
    if pathfoundandmincost(path,goal):
        mincost=path['1'][-1]
        for p in path:
            if path[p][-1]<mincost:
                result=path[p][0:len(path[p])-1]
                mincost=path[p][-1]
    deleteglobalmap()
    return result

# This function goes through the current path list and returns a path that reaches the goal and is least path value
def returnleastvaluepath(sendpath,path):
    
    for p in sendpath:
        if sendpath[p][-2]!=goal:
            path.pop(p,None)
    
    #print("Paths with only goals at ends:", path)
    tempindex=next(iter(path))
    #tempindex=list(path)[0]
    leastval=path[tempindex][-1]
    result=tempindex
    #print("leastval", leastval)
    for p in path:
        curval=path[p][-1]
        if curval<leastval:
            leastval=curval
            result=p
    #print("Path returning:", path[result][0:-1])
    #show_map(M, start, goal, path[result][0:-1])
    return path[result][0:-1]

# Declare global variables
def setglobalmap(Mlocal, goal_local, start_local):
    global M
    global goal
    global explored
    global frontier
    global start
    M=Mlocal
    goal=goal_local
    start=start_local

# Declare global variables
def deleteglobalmap():
    global M
    global goal
    global explored
    global frontier
    global start
    M=0
    goal=0
    start=0
    explored=[]
    frontier=[]
    
# Euclidian distance between two x-y coordinates: Sqrt((x2-x1)^2+(y2-y1)^2)
def direct_dist(a,b):
    return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)

# This function calculates total path cost(g) = path cost the last node(f) + direct cost fron last node to goal (h)
def findmincost(path):
    mincost=0
    if len(path)==1:
        mincost=mincost+direct_dist(M.intersections[path[0]],M.intersections[goal])
        return mincost
    for l in range(len(path)-1):
        mincost=mincost+direct_dist(M.intersections[path[l]],M.intersections[path[l+1]])
    
    mincost=mincost+direct_dist(M.intersections[path[len(path)-1]],M.intersections[goal])
        
    return mincost

def pathfoundandmincost(path,goal):
    minindex=next(iter(path))
    #minindex=list(path)[0]
    minval=path[minindex][-1]
    goalpath='0'
    for p in path:
        if path[p][-1]<minval:
            minval=path[p][-1]
            minindex = p
    for p in path:
        if path[p][-2]==goal:
            goalfound=True
            goalpath=p
    
    if goalpath==minindex:
        return True
    else:
        return False

def whattoexpandnext(path):
    minval=0
    expnd=0
    for p in path:
        if path[p][-2] not in explored:
            if path[p][-2] != goal:
                minval=path[p][-1]
                expnd=p
    for p in path:    
        if path[p][-1]<minval:
            if path[p][-2] not in explored:
                if path[p][-2] != goal:
                    if len(M.roads[path[p][-2]])>0:
                        expnd=p
                        minval=path[p][-1]
    return expnd

def expandedpath(path,roads,ex):

    exppath=copy.deepcopy(path)
    curlengthofpath=len(path)
    curpath=[]
    exoriginal=0
    exoriginal=ex
    curpath=copy.deepcopy(path[ex][0:-1])
    curmincost=0
    curmincost=copy.deepcopy(path[ex][-1])
    for r in range(len(roads)):
        if r==0:
            exppath[ex]=curpath
            exppath[ex].append(roads[r])
            exppath[ex].append(findmincost(exppath[ex]))
            ex=curlengthofpath+1
        else:
            exppath[str(ex)]=path[exoriginal][0:-1]
            exppath[str(ex)].append(roads[r])
            exppath[str(ex)].append(findmincost(exppath[str(ex)]))
            ex=ex+1
    return exppath