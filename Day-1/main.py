

def part1(captcha):
    totalSum = 0
    inputLength = len(captcha)
    for i in range(inputLength):
        curChar = captcha[i]
        nextChar = captcha[(i + 1)%inputLength]
        if(curChar == nextChar):
            totalSum += int(curChar)
    print("Sum for part 1: " + str(totalSum))

def part2(captcha):
    totalSum = 0
    inputLength = len(captcha)
    for i in range(inputLength):
        curChar = captcha[i]
        nextChar = captcha[(i + int(inputLength/2))%inputLength]
        if(curChar == nextChar):
            totalSum += int(curChar)
    print("Sum for part 2: " + str(totalSum))



if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().strip()
    part1(inputString)
    part2(inputString)


