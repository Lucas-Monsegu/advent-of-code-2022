class Node:
    def __init__(self, altitude,y,x):
        self.visited = False
        self.value = 1000000000
        self.y =y
        self.x =x
        if altitude == 'S':
            altitude = 'a'
        elif altitude == 'E':
            altitude = 'z'
        self.altitude = ord(altitude) - ord('a')
        self.previous = None
    def __repr__(self):
        return str(self.value)


def print_tab(tab):
    for line in tab:
        print(''.join(str(line[x])for x in range(len(line))))

def print_path(tab, endY, endX):
    m = [['.']* len(l)for l in tab]
    
    c = tab[endY][endX]
    while c.value != 0:
        m[c.y][c.x] = 'X'
        c = c.previous

    for i in m: print(''.join(i))

def get_neighboors(tab, y, x):
    l = []
    c = tab[y][x]
    if y+1 < len(tab) and (tab[y+1][x].altitude - c.altitude) < 2:
        l.append(tab[y+1][x])
    if y-1 >= 0  and (tab[y-1][x].altitude - c.altitude) < 2:
        l.append(tab[y-1][x])
    if x+1 < len(tab[0]) and (tab[y][x+1].altitude - c.altitude) < 2:
        l.append(tab[y][x+1])
    if x-1 >= 0 and (tab[y][x-1].altitude - c.altitude) < 2:
        l.append(tab[y][x-1])
    tab[y][x].visited = True
    return l



with open('input.txt') as f:
    lines = f.readlines()
tab = [[Node(lines[y][x], y, x) for x in range(len(lines[y].strip()))] for y in range(len(lines))]


endY = next(i for i in range(len(lines)) if 'E' in lines[i])
endX = next(i for i in range(len(lines[endY])) if lines[endY][i] == 'E')


m = 100000000
print("NUMBER OF STARTERS",len([(x,y)for y in range(len(tab))  for x in range(len(tab[0]))if tab[y][x].altitude==0]))
c=0
for x,y in [(x,y)for y in range(len(tab))  for x in range(len(tab[0]))if tab[y][x].altitude==0]:
    tab = [[Node(lines[y][x], y, x) for x in range(len(lines[y].strip()))] for y in range(len(lines))]
    print(c)
    c+=1
    neighboors = [tab[y][x]]
    neighboors[0].value = 0
    while len(neighboors) > 0:
        current = neighboors.pop(0)
        if current.visited:
            continue
        c_neighboors =  get_neighboors(tab, current.y, current.x)
        for neighboor in c_neighboors:
            if  current.value + 1 < neighboor.value:
                neighboor.value = current.value + 1
                neighboor.previous = current
        neighboors += list(filter(lambda x: not x.visited, c_neighboors))
        neighboors.sort(key=lambda x: x.value)
    m = min(m,tab[endY][endX].value)

print(m)