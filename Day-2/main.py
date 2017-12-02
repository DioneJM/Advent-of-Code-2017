
def part1(inp):
    checksum = 0
    for lines in inp:
        numList = list(map(int, lines.split(' ')))
        checksum += max(numList) - min(numList) 

    print(checksum)


def part2(inp):
    checksum = 0
    for lines in inp:
        numList = list(map(int, lines.split(' ')))
        for focus in numList:
            for other in numList:
                if(focus%other == 0 and focus != other):
                    checksum += focus/other

    print(checksum)


if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().splitlines()
    test = inputString[0].split(' ')
    part1(inputString)
    part2(inputString)
