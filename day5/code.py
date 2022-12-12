# <!-- --- Day 5: Supply Stacks ---

# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3

# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3

# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3

# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack? -->


#create stacks
file = open('input.txt', 'r')

instructions = []

for line in file:
    line = line.replace('\n', '')
    newline = line.split(" ")
    if newline[0] == "move":
        instructions.append(newline)

stack1 = ["V", "J", "B", "D"]
stack2 = ["F", "D", "R", "W", "B", "V", "P"]
stack3 = ["Q", "W", "C", "D", "L", "F", "G", "R"]
stack4 = ["B", "D", "N", "L", "M", "P", "J", "W"]
stack5 = ["Q", "S", "C", "P", "B", "N", "H"]
stack6 = ["G", "N", "S", "B", "D", "R"]
stack7 = ["H", "S", "F", "Q", "M", "P", "B", "Z"]
stack8 = ["F", "L", "W"]
stack9 = ["R", "M", "F", "V", "S"]

stacks = [stack1, stack1, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

#if we see a blank spot pop the next 4 and then check next char


for item in instructions:
    item.pop(0)
    item.pop(1)
    item.pop(2)
    print(item)


#4 spaces is one space in the stack

# for item in stackinfo:
#     for index, char in enumerate(item):
#         if char != ' ':

#     print(len(item))

# print(stackinfo)
