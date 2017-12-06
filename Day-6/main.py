
def distribute(blocks):
    states = set()
    currentState = blocks
    cycles = 0
    firstOcc = -1
    count = 0
    findState = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]
    while tuple(currentState) not in states:
        states.add(tuple(currentState))
        biggest = max(blocks)
        indBiggest = blocks.index(biggest)
        if(indBiggest + 1 > len(blocks) - 1):
            index = 0
        else:
            index = indBiggest + 1
        if (biggest) <= (len(blocks) - 1):
            toRemove = biggest
        else:
            toRemove = biggest - 1 
        blocks[indBiggest] -= toRemove
        while toRemove > 0:
            if index != indBiggest:
                blocks[index] += 1
            if (index + 1) > (len(blocks) -1): #has reached the end
                index = 0
            else:
                index += 1
            toRemove -= 1
       
        count += 1
        if currentState == findState and firstOcc < 0:
            firstOcc = count
        currentState = blocks
        cycles += 1
    
    diff = cycles - firstOcc
    print("Took: " + str(cycles) + " cycles until the state repeated") #Part 1
    print("# of cycles between first and second occurence of state = " + str(diff)) #Part 2


if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().split()

    memBlocks = list(map(int, inputString))
    out = distribute(memBlocks)

