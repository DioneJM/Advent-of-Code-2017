
from itertools import cycle
import operator



def generate_grids(find, size):
    if find > size :
        return (None, None)

    node = 1
    grid = {(0, 0) : 1}
    nodeSum = 1
    summedGrid = {(0, 0) : 1}
    position = (0,0)
    numSteps = 1 #The number of steps wheng going a certain direction
    turns = 2 #Max number of turns before number of steps increases
    #Right -> Up -> Left -> Down
    direction = cycle([(1, 0),(0 , 1),(-1, 0),(0, -1)]) 
    partA = 0
    partB = 0
    bFound = False

    while True:
        for t in range(turns):
            move = next(direction)
            for step in range(numSteps):
                node += 1

                #grid for part1
                grid[str(position)] = node

                #grid for part2
                nodeSum = neighbourSum(position, summedGrid)
                summedGrid[position] = nodeSum

                position = (position[0] + move[0],position[1] + move[1]) 

                if node == find:
                    partA = abs(position[0]) + abs(position[1])
                if nodeSum > find:
                    if not bFound:
                        partB = nodeSum
                        bFound = True
                if node > size:
                    return (partA, partB)
        numSteps += 1
    return (partA, partB)

def neighbourSum(position, grid):
    #(x-1,y+1)|(x,y+1)|(x+1,y+1)
    #(x-1,y) | (x,y) | (x+1,y)
    #(x)-1,y-1)|(x,y-1)|(x+1,y-1)
    if position == (0,0):
        return 1
    neighbourSum = 0
    #relative position of all neighbours
    neighbourLoc = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]    
    #print(grid.items())
    for n in neighbourLoc:
        nCoord = (position[0] + n[0], position[1] + n[1])
        if nCoord in grid:
            neighbourSum += grid[nCoord]

    return neighbourSum
    


if __name__ == "__main__":
    _input = 347991
    (partA, partB) = generate_grids(_input, _input)
    print("Part 1: " + str(partA))
    print("Part 2: " + str(partB))


