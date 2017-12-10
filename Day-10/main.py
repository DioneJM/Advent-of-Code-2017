from itertools import cycle


def knotHash(size, lengths, iterations):
    inpList = list(range(size))
    listLen = len(inpList)
    product = 0
    skipSize = 0
    curInd = 0
    move = 0
    for i in range(iterations):  
        for length in lengths:
            index = curInd
            subList = [None]*length
            for i in range(length):
                subList[i] = inpList[(index+i)%len(inpList)]
            offset = 0
            for num in reversed(subList):
                inpList[(index+offset)%len(inpList)] = num
                offset += 1
            move = length + skipSize
            curInd += move
            skipSize += 1

    product = inpList[0]*inpList[1]
    print("Product:", product)

    if iterations == 64:
        knotHash = str()
        for block in range(listLen//16):
            denseVal =  0
            for sparse in range(16):
                denseVal ^= inpList[block * 16 + sparse]
            knotHash += hex(denseVal)[2:].zfill(2)

        print("Knot Hash:", knotHash)
        print("Iterations:", iterations)
if __name__ == "__main__":
    maxVal = 256#256 for puzzle
    fileIn = open("input.txt").read()
    hashKey1 = [int(i) for i in fileIn.strip().split(",")]
    hashKey2 = [ord(x) for x in fileIn.strip()] + [17, 31, 73, 47, 23]
    testHash = [ord(c) for c in "AoC 2017"] +  [17, 31, 73, 47, 23]

    print("-----")
    print("Running for part 1...")
    knotHash(maxVal, hashKey1, 1)
    print("-----")
    print("Running for part 2...")
    knotHash(maxVal, hashKey2, 64)
    print("-----")
    


