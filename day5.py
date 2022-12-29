def get_nb_stack(lines):
    for i in lines:
        if '1' in i:
            return max(map(int,i.split()))

def split_by_tree(line):
    return [line[i:i+3] for i in range(0,len(line),4)]

def move_multiple(cola, colb, stacks, number):
    els = [stacks[cola].pop()for i in range(number)][::-1]
    for el in els:
        stacks[colb].append(el)
    

with open('input.txt', 'r') as f:
    lines = f.readlines()
    nb_stacks = get_nb_stack(lines)         
    stacks = []
    for line in lines:
        if '1' in line:
            break  
        stacks += [split_by_tree(line)]
    stacks = list(zip(*stacks))
    stacks = [list(reversed(stack)) for stack in stacks]
    for stack in stacks:
        while '   ' in stack:
            stack.remove('   ')
    for line in filter(lambda x: 'move' in x, lines):
        number, cola, colb = list(map(int,filter(lambda x: x.isnumeric(), line.split())))
        move_multiple(cola-1, colb-1, stacks, number)
    print(''.join(stack[-1][1] for stack in stacks))