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
file = open('sampleinput.txt', 'r')

instructions = []
stackinfo = []

for line in file:
    line = line.replace('\n', '')
    newline = line.split(" ")
    if newline[0] == "move":
        instructions.append(newline)
    else:
        stackinfo.append(newline)

for ind, item in enumerate(stackinfo):
    numspaces = 0
    topop = []
    for index, char in enumerate(item):
        if char == '':
            numspaces += 1
            if numspaces == 4:
                numspaces = 0
            else:
                topop.append(index)
    popped = 0
    newitem = item
    for num in topop:
        newitem.pop(num-popped)
        popped += 1
    stackinfo[ind] = newitem


finalline = stackinfo[len(stackinfo)-2]
numstacks = []

for item in finalline:
    if item != '':
        numstacks.append(item)
stackinfo[len(stackinfo)-2] = numstacks
        
#create each stack
stacks = []
for i in range(len(numstacks)):
    stacks.append([])

stackinfo = stackinfo[:-2]

for item in stackinfo:
    for i in range(len(item)):
        stacks[i].append(item[i])

#FINALLY HAVE MADE STACKS
# for item in stacks:
#     print(item)

#NOW EXECUTE INSTRUCTIONS ON STACKS
for item in instructions:
    numtomove = int(item[1])
    #subtract 1 to account for index
    leaving = int(item[3]) - 1
    entering = int(item[5]) - 1
    moving = []
    #get whats leaving and remove from current stack
    for index, char in enumerate(stacks[leaving]):
        if char != '' and numtomove != 0:
            moving.append(char)
            numtomove -=1 
            stacks[leaving][index] = ''
    ind = len(stacks[entering]) - 1
    while len(moving) > 0:
        if stacks[entering][ind] == '':
            stacks[entering][ind] = moving[0]
            moving.pop(0)
        elif ind < 0:
            stacks[entering].insert(0,moving[0])
            moving.pop(0)
        ind -= 1
        

print(stacks)
        
    