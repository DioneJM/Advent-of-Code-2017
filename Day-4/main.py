

def alphabetize(string):
    newString = list(string)
    newString.sort()
    result = ''.join(newString)
    return result


def verify_password(passwords):
    part1 = 0
    part2 = 0
    for p in passwords: #each line of input
        split = p.split()
        #convert to set to remove multiple characters and then back to list to compare 
        #with the original
        pSet = list(set(split)) 
        if len(pSet) == len(split):
            part1 += 1
            
            #part 2
            anagram = 0
            s = p.split(" ")
            index = 0
            for word in s[index:len(s)]: #grab a word from each line
                #convert current word to an alphabetical list of characters
                words = alphabetize(word)
                for other in s[index+1:len(s)]: #compare word with other words in the line
                    #convert other words to alphabetical list of characters
                    others= alphabetize(other)
                    if words == others: #check if anagram (have the same contents)
                        anagram += 1
                index += 1
            if anagram == 0:
                part2 += 1
    return (part1, part2)


if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().splitlines()
    test = inputString
    out = verify_password(test)
    print("Part1: " + str(out[0]) + "\nPart2: " + str(out[1]))
    #part2(inputString)
