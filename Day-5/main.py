
def execute_instruction(instructions):

    steps = 0
    curIndex = 0
    while curIndex < len(instructions) and curIndex >= 0:
        curInstr = int(instructions[curIndex]) #gets the value of the instr pointed by index
        if curInstr >= 3:
            instructions[curIndex] -= 1
        else:
            instructions[curIndex] += 1 #remove conditional and keep this line for part 1
        curIndex += curInstr #update where the index is pointing to
        steps += 1
    return steps

if __name__ == "__main__":
    with open("input.txt") as f:
        inputString = f.read().splitlines()
    steps_needed = execute_instruction(list(map(int, inputString)))
    print("steps needed = " + str(steps_needed))
