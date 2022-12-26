from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    lines = f.readlines()

scan = [list(map(lambda x: int(x),line.split(',')))for line in lines]

def get_faces_of_cube(x,y,z):
    return {
    (x - 1, x, y, y, z, z),
    (x, x + 1, y, y, z, z),
    (x, x, y - 1, y, z, z),
    (x, x, y, y + 1, z, z),
    (x, x, y, y, z - 1, z),
    (x, x, y, y, z, z + 1)
  }

def get_neigbhors(x,y,z):
    return {
        (x-1,y,z),
        (x+1,y,z),
        (x,y-1,z),
        (x,y+1,z),
        (x,y,z-1),
        (x,y,z+1)
    }

def get_air_pockets():
    q = deque()
    start = (0,0,0)
    q.append(start)
    air_pockets = set()
    while q:
        lava = q.popleft()
        negs = get_neigbhors(*lava)
        for n in negs:
            if n[0] >= 0 and n[1] >= 0 and n[2] >= 0 and n[0] < GRID_SIZE and n[1] < GRID_SIZE and n[2] < GRID_SIZE and n not in scan and n not in air_pockets:
                air_pockets.add(n)
                q.append(n)
    return air_pockets



GRID_SIZE = 21


air_pockets = get_air_pockets()

def get_faces(list_of_points):
    faces = defaultdict(int)
    for x,y,z in list_of_points:
        line_faces = get_faces_of_cube(x, y, z)
        for f in line_faces: faces[f] += 1
    return faces 

faces_lava = get_faces(scan)
print('nb faces lava',sum(1 for i in faces_lava.values() if i == 1))
faces_air = get_faces(air_pockets)
print('nb faces air', sum(1 for i in faces_air.values() if i == 1))