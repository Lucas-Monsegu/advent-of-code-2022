import itertools

with open('input.txt') as f:
    lines = f.readlines()

class Mine:
    def __init__(self, segments):
        self.minX = min(i[0] for i in itertools.chain(*segments))
        self.maxX = max(i[0] for i in itertools.chain(*segments))
        self.minY = min(i[1] for i in itertools.chain(*segments))
        self.maxY = max(i[1] for i in itertools.chain(*segments))
        self.segments = segments
        self.tab = [['.']* ( self.maxX*2)for i in range(self.maxY+3)]
        for x in range(len(self.tab[0])):
            self.tab[-1][x] = '#'

    def __repr__(self):
        s=''
        for i in self.tab:
            s+= ''.join(str(x) for x in i[self.minX-2:])+'\n'
        return s

    def draw_lines(self):
        for segment in segments:
            startX, startY = segment[0]
            for line in segment[1:]:
                endX, endY = line
                for i in range(min(startX,endX), max(startX,endX)+1):
                    self.tab[startY][i] = '#'
                for i in range(min(startY,endY), max(startY,endY)+1):
                    self.tab[i][startX] = '#'
                startX, startY = endX, endY
    
    def fall_a_grain(self):
        def fall_once(y,x, falled):
            if y+1 >= len(self.tab):
                return False
            elif self.tab[y+1][x] == '.':
                return fall_once(y+1, x, True)
            elif x-1 >= 0 and self.tab[y+1][x-1] == '.' and falled:
                return fall_once(y, x-1, False)
            elif x+1 < len(self.tab[0]) and self.tab[y+1][x+1] == '.' and falled:
                return fall_once(y, x+1, False)
            if self.tab[y][x] == '.':
                self.tab[y][x] = 'o'
                return True
            return False
        return fall_once(0, 500, True)
    
    def res(self):
        return sum(i.count('o') for i in self.tab)

segments = []
for line in lines:
    segments += [[list(map(int,i.split(','))) for i in line.split(' -> ')]]

m = Mine(segments)
m.draw_lines()
c = 0
while m.fall_a_grain():
    c+=1
# print(m)
print(m.res())    
