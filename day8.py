
def count_trees_horizontal(y,start, end, step, treesize):
    c = 1
    for x in range(start, end, step):
        if x == start:
            continue
        tree = lines[y][x]
        if tree >= treesize:
            return c
        c+=1

    return c -1
        
def count_trees_vertical(x, start, end, step, treesize):
        c = 1
        for y in range(start, end, step):
            if y == start:
                continue
            tree = lines[y][x]
            if tree >= treesize:
                return c
            c+=1
            
        return c -1

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [list(map(int,line.replace('\n',''))) for line in lines]
    seen_trees = [[0 for i in range(len(lines))]for line in range(len(lines))]
    # pr.int('left')
    r = 0 
    for y in range(len(lines)):
        for x in range(len(lines)):

            t = [
            count_trees_horizontal(y, x, len(lines), 1, lines[y][x]),
            count_trees_horizontal(y, x, -1, -1, lines[y][x]),
            count_trees_vertical(x, y, len(lines), 1, lines[y][x]),
            count_trees_vertical(x, y, -1, -1, lines[y][x])
            ]
            v = eval('*'.join(map(str,t)))
            r=max(r,v)  
    print(r)