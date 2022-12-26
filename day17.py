with open('input.txt') as f:
    lines = f.readlines()

a = [33904, 33926, 34019, 34097, 34298, 34331, 34339, 34372, 34396, 34404, 34429, 34500, 34507, 34682, 34719, 34770, 34782, 34845, 34897, 34924, 35000, 35079, 35117, 35123, 35186, 35229, 35297, 35348, 35459, 35575, 35583, 35650, 35730, 35764, 35807, 35937, 36053, 36171, 36174, 36177, 36197, 36199, 36255, 36455, 36529, 36600, 36632, 36654, 36747, 36825, 37026, 37059, 37067, 37100, 37124, 37132, 37157, 37228, 37235, 37410, 37447, 37498, 37510, 37573, 37625, 37652, 37728, 37807, 37845, 37851, 37914, 37957, 38025, 38076, 38187, 38303, 38311, 38378, 38458, 38492, 38535, 38665, 38781, 38899, 38902, 38905, 38925, 38927, 38983, 39183, 39257, 39328, 39360, 39382, 39475, 39553, 39754, 39787, 39795, 39828, 39852, 39860, 39885, 39956, 39963, 40138, 40175, 40226, 40238, 40301, 40353, 40380, 40456, 40535, 40573, 40579, 40642, 40685, 40753, 40804, 40915, 41031, 41039, 41106, 41186, 41220, 41263, 41393, 41509, 41627, 41630, 41633, 41653, 41655, 41711, 41911, 41985, 42056, 42088, 42110, 42203, 42281, 42482, 42515, 42523, 42556, 42580, 42588, 42613, 42684, 42691, 42866, 42903, 42954, 42966, 43029, 43081, 43108, 43184, 43263, 43301, 43307, 43370, 43413, 43481, 43532, 43643, 43759, 43767, 43834, 43914, 43948, 43991, 44121, 44237, 44355, 44358, 44361, 44381, 44383, 44439, 44639, 44713, 44784, 44816, 44838, 44931, 45009, 45210, 45243, 45251, 45284, 45308, 45316, 45341, 45412, 45419, 45594, 45631, 45682, 45694, 45757, 45809, 45836, 45912, 45991, 46029, 46035, 46098, 46141, 46209, 46260, 46371, 46487, 46495, 46562, 46642, 46676, 46719, 46849, 46965, 47083, 47086, 47089, 47109, 47111, 47167, 47367, 47441, 47512, 47544, 47566, 47659, 47737, 47938, 47971, 47979, 48012, 48036, 48044, 48069, 48140, 48147, 48322, 48359, 48410, 48422, 48485, 48504, 48522, 48553, 48679, 48771, 48782, 48797, 48849, 48865, 48873, 48970, 48996, 49120, 49173, 49176, 49269, 49379, 49398, 49473, 49483, 49571, 49579, 49672, 49724, 49742, 49744, 49956, 49989, 49999]
c={}
for i in range(len(a)):
    for j in range(len(a)):
        key = a[i] - a[j]
        if key <= 0:continue
        if key not in c:
            c[key] = 0
        c[key] += 1
max_key = max(c.keys(),key=lambda x: c[x])
print(max_key, c[max_key])
# exit()
ROCKS = [
    [[True] * 4],
    [[False, True, False], [True, True, True], [False, True, False]],
    [[False, False, True], [False, False, True], [True, True, True]],
    [[True], [True], [True], [True]],
    [[True, True], [True, True]]
]

class Rock:

    def __init__(self, rock, tower):
        self.tower = tower
        self.rock = rock
        self.indexes = []

        for y in range(len(rock)):
            for x in range(len(rock[0])):
                tower[len(tower)-tower_size-3-len(rock)+y][x+2] = rock[y][x]
                if rock[y][x]:
                    self.indexes.append([len(tower)-tower_size-3-len(rock)+y, x+2])

    def move_right(self):
        cpy = [*self.indexes]
        for y,x in cpy:
            if [y,x+1] in cpy:continue
            if x+1 >= len(self.tower[0]) or self.tower[y][x+1] != False: return False
        for i in range(len(cpy)):
            y,x = cpy[i]
            cpy[i] = [y, x+1]
        for y,x in self.indexes: tower[y][x] = False
        for y,x in cpy: tower[y][x] = True
        self.indexes = cpy
        return True

    
    def move_left(self):
        cpy = [*self.indexes]
        for y,x in cpy:
            if [y,x-1] in cpy:continue
            if x-1 < 0 or self.tower[y][x-1] != False: return False
        for i in range(len(cpy)):
            y,x = cpy[i]
            cpy[i] = [y, x-1]
        for y,x in self.indexes: tower[y][x] = False
        for y,x in cpy: tower[y][x] = True
        self.indexes = cpy
        return True
    
    def move_from_jet(self, direction):
        if direction == '<':
            return self.move_left()
        else:
            return self.move_right()

    def move_down(self):
        cpy = [*self.indexes]
        for y,x in cpy:
            if [y+1,x] in cpy:continue
            if y+1 >= len(self.tower) or self.tower[y+1][x] != False: return False

        for i in range(len(cpy)):
            y,x = cpy[i]
            cpy[i] = [y+1, x]
        for y,x in self.indexes: tower[y][x] = False
        for y,x in cpy: tower[y][x] = True
        self.indexes = cpy
        return True


def get_surface():
    l = [0]*7
    c=0
    for y in range(len(tower)-tower_size - 3, len(tower), 1):
        for x in range(7):
            if tower[y][x]:
                if not l[x]:
                    l[x] = c
        c+=1
    return tuple(l)

tower = [[False] * 7 for i in range(5000)]
rock_counter = 0
tower_size = 0
pattern, pattern_index = lines[0], 0
patterns = {}
for i in range(1000):
    print('------------')
    current_rock_form = ROCKS[rock_counter]
    
    hashing_key = (get_surface(),pattern[pattern_index], rock_counter)
    if hashing_key in patterns:
        print('found pattern !', i, hashing_key)
        patterns[hashing_key] += 1
    else:
        patterns[hashing_key] = 1
    rock_counter = ( rock_counter +1 ) % len(ROCKS)
    rock = Rock(current_rock_form, tower)
    # print(i, current_rock_form)
    down_count = 0
    while True:
        rock.move_from_jet(pattern[pattern_index])
        pattern_index = (pattern_index+1) % len(pattern)
        if not rock.move_down():
            break
        down_count +=1
    c = 0
    if not i%1000:print(i)
    for i in range(len(tower)-1, -1, -1):
        if True not in tower[i]:
            break
        else: c+=1
    tower_size = c
    # for t in tower: print(' '.join('#' if x else '.' for x in t))
print(tower_size)
print(max(patterns.values()))