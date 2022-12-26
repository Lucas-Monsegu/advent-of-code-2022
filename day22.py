import re


def go_right(pos, face, direction):
    y, x = pos
    x = x + 1
    if x >= SIZE:
        direction, face, y, x = get_new_pos(direction, face, y, x - 1)
    if faces[face][y][x] == "#":
        return False
    faces[face][y][x] = ">"
    return direction, face, y, x


def go_left(pos, face, direction):
    y, x = pos
    x = x - 1
    if x < 0:
        direction, face, y, x = get_new_pos(direction, face, y, x + 1)
    if faces[face][y][x] == "#":
        return False
    faces[face][y][x] = "<"
    return direction, face, y, x


def go_down(pos, face, direction):
    y, x = pos
    y = y + 1
    if y >= SIZE:
        direction, face, y, x = get_new_pos(direction, face, y - 1, x)
    if faces[face][y][x] == "#":
        return False
    faces[face][y][x] = "v"
    return direction, face, y, x


def go_up(pos, face, direction):
    y, x = pos
    y = y - 1
    if y < 0:
        direction, face, y, x = get_new_pos(direction, face, y + 1, x)
    if faces[face][y][x] == "#":
        return False
    faces[face][y][x] = "^"
    return direction, face, y, x


letter_to_angle = {"L": -1, "R": 1}
dirs = "RDLU"
direction = 0
dir_to_func = {"R": go_right, "L": go_left, "D": go_down, "U": go_up}


def move(times, pos, face, direction):
    for i in range(int(times)):
        r = dir_to_func[direction](pos, face, direction)
        if r == False:
            break
        direction, face, *pos = r
    return direction, face, pos


def get_new_pos(direction, current_face, y, x):
    if current_face == 0:
        t = {
            "R": ("R", 1, y, 0),
            "D": ("D", 2, 0, x),
            "L": ("R", 3, 49 - y, 0),
            "U": ("R", 5, x, 0),
        }
    if current_face == 1:
        t = {
            "L": ("L", 0, y, 49),
            "D": ("L", 2, x, 49),
            "R": ("L", 4, 49 - y, 49),
            "U": ("U", 5, 49, x),
        }
    if current_face == 2:
        t = {
            "U": ("U", 0, 49, x),
            "R": ("U", 1, 49, y),
            "L": ("D", 3, 0, y),
            "D": ("D", 4, 0, x),
        }
    if current_face == 3:
        t = {
            "L": ("R", 0, 49 - y, 0),
            "U": ("R", 2, x, 0),
            "R": ("R", 4, y, 0),
            "D": ("D", 5, 0, x),
        }
    if current_face == 4:
        t = {
            "R": ("L", 1, 49 - y, 49),
            "U": ("U", 2, 49, x),
            "L": ("L", 3, y, 49),
            "D": ("L", 5, x, 49),
        }
    if current_face == 5:
        t = {
            "L": ("D", 0, 0, y),
            "D": ("D", 1, 0, x),
            "U": ("U", 3, 49, x),
            "R": ("U", 4, 49, y),
        }
    return t[direction]


with open("input.txt") as f:
    lines = list(map(lambda x: x.replace("\n", ""), f.readlines()))


path = lines[-1]
path = re.findall(r"([0-9]+|[A-Z])", path)
board = lines[:-2]
SIZE = max(len(x) for x in board)
for y in range(len(board)):
    board[y] = [*board[y].ljust(SIZE, " ")]
SIZE = SIZE // 3
faces = [
    [
        [board[y][x] for x in range(min_x, min_x + SIZE)]
        for y in range(min_y, min_y + SIZE)
    ]
    for min_y, min_x in [
        (0, SIZE),
        (0, SIZE * 2),
        (SIZE, SIZE),
        (2 * SIZE, 0),
        (2 * SIZE, SIZE),
        (3 * SIZE, 0),
    ]
]

face = 0
pos = 0, next(x for x in range(SIZE) if faces[face][0][x] == ".")
for i in faces:
    for x in i:
        print("".join(x))
    print("-----------------------")

for i in path:
    if i.isalpha():
        direction = direction + letter_to_angle[i]
        direction = len(dirs) - 1 if direction < 0 else direction % len(dirs)

        continue
    direction, face, pos = move(i, pos, face, dirs[direction])
    direction = dirs.index(direction)
for i in faces:
    for x in i:
        print("".join(x))
    print("-----------------------")

print(list(map(lambda x: x + 1, pos)), face, direction)
# print((pos[0] + 1) * 1000 + 4 * (pos[1] + 1) + direction)
