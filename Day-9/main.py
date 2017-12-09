
def processGroup(stack):

    level = 0
    score = 0
    prevChar = None
    garbage = False
    groups = 0
    ignore = False
    garbCount = 0
    for c in range(len(stack)):
        char = stack[c]
        if ignore == True and garbage == True:
            ignore = False
            continue
        elif char == '!': 
            ignore = True
        elif garbage == True:
            if char == '>':
                garbage = False
            else:
                garbCount += 1
        elif char == '<':
            garbage = True
        elif char == '{':
            level += 1
        elif char == '}':
            score += level
            level -= 1
            groups += 1
        prevChar = char
    print("number of groups: ", groups)
    return (score, garbCount)

if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.readline()
    inp = str(inputString)
    score = processGroup(inp)
    print('Part 1 score: ', score[0])
    print('Part 2 score: ', score[1])
