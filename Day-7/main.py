

class Tree(object):
    def __init__(self):
        self.weight = 0
        self.children = list()

def createGraph(programList):
    
    graph = dict()
    for program in programList:
        prg = program.split("-> ")
        node = prg[0].split(" ")
        name = node[0]
        weight = node[1].strip("()")
        if(len(prg) >= 2):
            children = prg[1].split(", ")
        else:
            children = []
        elem = Tree()
        elem.weight = int(weight)
        elem.children = children
        graph[name] = elem

    #Find root of graph
    root = str()
    for node in graph:
        notIn = 0
        for otherNodes in graph:
            children = graph[otherNodes].children
            if node in children:
                break
            else:
                notIn += 1
        if notIn == len(graph):
            root = node
    return (root, graph)

def findImbalance(root, graph):

    children = graph[root].children
    sumWeight = graph[root].weight
    if len(children) == 0:
        return sumWeight

    ideal = list()
    childrenWeightList = list()
    for child in children:
        curWeight = findImbalance(child, graph)
        sumWeight += curWeight
        ideal.append(curWeight)
        childrenWeightList.append(graph[child].weight)
    if len(set(ideal)) > 1:
        print('----------------')
        print('Found imbalance:')
        print(ideal)
        print(children)
        print(childrenWeightList)
        print('----------------')
    return sumWeight


if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().splitlines()
    inp = inputString
    testinp = inputString[5].split("->")
    out = createGraph(inp)
    root = out[0]
    print(root)
    graph = out[1]
    print("Program root = [{}]".format(root))
    findImbalance(root,graph)



