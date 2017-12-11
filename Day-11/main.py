
"""
Transformed the hex grid into a 2d plane
https://www.redblobgames.com/grids/hexagons/#distances-cube
NW|N |X
--+--+--
SW|  |NE
--+--+--
 X|S |SE
"""
def follow_path(path):
    stepsReq = 0
    xCoord = 0
    yCoord = 0
    distances = []
    for step in path:
        if step == "n":
            yCoord += 1
        if step == "s":
            yCoord -= 1
        if step == "nw":
            xCoord -= 1
            yCoord += 1
        if step == "se":
            xCoord += 1
            yCoord -= 1
        if step == "ne":
            xCoord += 1
        if step == "sw":
            xCoord -= 1
        stepsReq = (abs(xCoord) + abs(yCoord) + abs(xCoord + yCoord))/2
        distances.append(stepsReq)
    return (stepsReq, max(distances))
    
if __name__ == "__main__":
    fileIn = open("input.txt").read()
    inp = fileIn.strip().split(",")
    out = follow_path(inp)
    print("Part 1:\nDistance is:",out[0])
    print("Part 2:\nMax distance is:",out[1])
