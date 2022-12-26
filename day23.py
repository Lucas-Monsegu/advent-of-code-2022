from collections import Counter


class Info:
    ORDER = ["east", "west", "south", "north"]


class Elf:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.proposed_pos = None

    def __repr__(self):
        return f"{self.y} {self.x}"

    def move(self):
        if proposed_count[self.proposed_pos] > 1 or self.proposed_pos == None:
            self.proposed_pos = None
            return
        self.y = self.proposed_pos[0]
        self.x = self.proposed_pos[1]
        self.proposed_pos = None

    def update_proposed_pos(self):
        close_elfs = self.get_close_elfs()
        proposed_pos = None
        if len(close_elfs) == 0:
            self.proposed_pos = proposed_pos
            return
        for direction in Info.ORDER:
            if direction == "north":
                r = self.get_north(close_elfs)
            elif direction == "south":
                r = self.get_south(close_elfs)
            elif direction == "west":
                r = self.get_west(close_elfs)
            elif direction == "east":
                r = self.get_east(close_elfs)
            if r:
                proposed_pos = r

        self.proposed_pos = proposed_pos

    def get_north(self, close_elfs):
        return (
            (self.y - 1, self.x)
            if not any(elf for elf in close_elfs if elf.y < self.y)
            else None
        )

    def get_south(self, close_elfs):
        return (
            (self.y + 1, self.x)
            if not any(elf for elf in close_elfs if elf.y > self.y)
            else None
        )

    def get_west(self, close_elfs):
        return (
            (self.y, self.x - 1)
            if not any(elf for elf in close_elfs if elf.x < self.x)
            else None
        )

    def get_east(self, close_elfs):
        return (
            (self.y, self.x + 1)
            if not any(elf for elf in close_elfs if elf.x > self.x)
            else None
        )

    def get_close_elfs(self):
        return [
            elf
            for elf in elves
            if elf.y - 1 <= self.y <= elf.y + 1
            and elf.x - 1 <= self.x <= elf.x + 1
            and elf != self
        ]


def debug():
    for y in range(15):
        s = ""
        for x in range(15):
            c = "."
            for elf in elves:
                if elf.y == y and elf.x == x:
                    c = "#"
                    break
            s += c
        print(s)


def get_answer():
    min_x = min(elf.x for elf in elves)
    min_y = min(elf.y for elf in elves)
    max_x = max(elf.x for elf in elves)
    max_y = max(elf.y for elf in elves)
    c = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if any(elf.x == x and elf.y == y for elf in elves):
                c += 0
            else:
                c += 1
    return c


with open("input.txt") as f:
    lines = f.readlines()

board = [[*l.strip()] for l in lines]

elves = [
    Elf(y, x)
    for y in range(len(board))
    for x in range(len(board[y]))
    if board[y][x] == "#"
]
state_before = [Elf(elf.y, elf.x) for elf in elves]
i = 0
while True:
    print(i)
    for elf in elves:
        elf.update_proposed_pos()
    proposed_count = Counter(
        (elf.proposed_pos[0], elf.proposed_pos[1])
        for elf in elves
        if elf.proposed_pos != None
    )
    for elf in elves:
        elf.move()
    Info.ORDER = [Info.ORDER[-1]] + Info.ORDER[:-1]
    if Counter((elf.y, elf.x) for elf in elves) == Counter(
        (elf.y, elf.x) for elf in state_before
    ):
        print("answer is", i + 1)
        break
    i += 1
    state_before = [Elf(elf.y, elf.x) for elf in elves]
