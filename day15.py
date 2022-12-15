class Sond:
    def __init__(self,x,y, bx,by):
        self.x = x
        self.y = y
        self.beacon_x = bx
        self.beacon_y = by
        self.radius = abs(x-bx) + abs(y-by)

    def is_in_range(self, x,y) -> bool:
        if x == self.beacon_x and y == self.beacon_y:
            return False
        if abs(self.x - x) + abs(self.y - y) <= self.radius:
            return True
        return False
        
    
    def __repr__(self):
        return f'Sond: {self.x} {self.y} radius: {self.radius}'


with open('input.txt') as f:
    lines = f.readlines()

sonds = []
for line in lines:
    l = line.replace(',', '').replace(':', '').split()
    sx = int(l[2].split('=')[1])
    sy = int(l[3].split('=')[1])
    bx = int(l[8].split('=')[1])
    by = int(l[9].split('=')[1])
    sonds += [Sond(sx,sy,bx,by)]

y = 0
while y < 4000000:
    x = 0
    if y % 100000 == 0: print(y)
    while x < 4000000:
        for sond in sonds:
            if sond.is_in_range(x, y):
                # print('in range', sond)
                endx = (sond.x + sond.radius) - abs(sond.y-y)
                nx = endx
                x = nx
                break
        else:
            print('found distress', x,y)
        x += 1
    y+=1