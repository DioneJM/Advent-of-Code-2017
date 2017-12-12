from collections import *


def determineConnections(programs):
    queue = [0]
    hasZero = set()
    while queue:
        program = queue.pop()
        for connection in programs[program]:
            if connection not in hasZero:
                hasZero.add(connection)
                queue.append(connection)
    return len(hasZero)

def findGroups(programs):
    groupSet = set()
    groups = 0
    for program in range(len(programs)):
        if program in groupSet:
            continue
        groups += 1
        queue = [program]
        while queue:
            curProgram = queue.pop()
            for connection in programs[curProgram]:
                if connection not in groupSet:
                    groupSet.add(connection)
                    queue.append(connection)
    return groups

def main():
    programs = defaultdict(set)
    with open('input.txt') as f:
        for line in f:
            form = line.strip().split(" <-> ") 
            program = int(form[0])
            connections = set(map(int, form[1].split(", ")))
            for connection in connections:
                programs[program].add(connection)
                programs[connection].add(program)
    out = determineConnections(programs)
    print("Part 1: ", out)
    out2 = findGroups(programs)
    print("Part 2: ", out2)

main()
