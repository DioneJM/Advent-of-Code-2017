from collections import defaultdict

def process_instr(inp):
    registers = defaultdict(int)
    maxVal = 0
    for instr in inp:
        tar, command, num, iff, condLeft, condition, condRight = instr.split()
        if eval("registers[condLeft]" + condition + condRight):
            if command == "inc":
                registers[tar] += int(num)
            if command == "dec":
                registers[tar] -= int(num)

         
        if registers[tar] > maxVal:
            maxVal = registers[tar]
    
    curMaxVal = 0
    for reg in registers:
        if registers[reg] > curMaxVal:
            curMaxVal = registers[reg]

    print("Part 1: ", curMaxVal, "\nPart 2: ", maxVal)
if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().splitlines()
    inp = list(inputString)
    process_instr(inp)



