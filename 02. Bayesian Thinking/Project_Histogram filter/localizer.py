import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = [[] for i in range(len(beliefs))]
            
    #print color
    #print len(grid)
    #print beliefs
    #print p_hit
    #print p_miss
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            hit=(cell==color)
            new_beliefs[i].append(beliefs[i][j]*p_hit*hit+beliefs[i][j]*(1-hit)*p_miss)
            #if cell==color:
            #    new_beliefs[i].append(beliefs[i][j]*p_hit)
            #else:
            #    new_beliefs[i].append(beliefs[i][j]*p_miss)
    s=sum(sum(new_beliefs,[]))
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            new_beliefs[i][j]=new_beliefs[i][j]/s
    #
    # TODO - implement this in part 2
    #

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    #print new_G[0][3]
    #print new_G
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height #fix - previousltheight and width were interchanged
            new_j = (j + dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)