class Simulation:
    grid = [[]]
    history = {}

    @classmethod
    def get_grid(cls, turn):
        if turn in cls.history:
            return cls.history[turn]
        width = len(cls.grid[0])
        height = len(cls.grid)
        new_grid = [[[] for x in line] for line in cls.grid]
        for y in range(height):
            for x in range(width):
                vals = cls.grid[y][x]
                for val in vals:
                    if val == ">":
                        new_grid[y][(x + 1) % width].append(val)
                    if val == "<":
                        new_grid[y][x - 1 if x - 1 >= 0 else width - 1].append(val)
                    if val == "v":
                        new_grid[(y + 1) % height][x].append(val)
                    if val == "^":
                        new_grid[y - 1 if y - 1 >= 0 else height - 1][x].append(val)
        cls.history[turn] = new_grid
        cls.grid = new_grid
        print("new_grid", turn)
        return cls.history[turn]

    @classmethod
    def debug(cls, turn):
        grid = cls.history[turn]
        for y in range(len(grid)):
            s = ""
            for x in range(len(grid[y])):
                if len(grid[y][x]) == 0:
                    s += "."
                elif len(grid[y][x]) == 1:
                    s += grid[y][x][0]
                else:
                    s += str(len(grid[y][x]))
            print(s)
        print("------------------------------------------")


class Path:
    @classmethod
    def get_movable_squares(cls, y, x, grid):
        squares = []
        if y < 0:
            if y + 1 < len(grid) and len(grid[y + 1][x]) == 0:
                squares.append((y + 1, x))
            squares.append((y, x))
            return squares
        if y >= len(grid):
            if y - 1 >= 0 and len(grid[y - 1][x]) == 0:
                squares.append((y - 1, x))
            squares.append((y, x))
            return squares
        if y - 1 >= 0 and len(grid[y - 1][x]) == 0:
            squares.append((y - 1, x))
        if y + 1 < len(grid) and len(grid[y + 1][x]) == 0:
            squares.append((y + 1, x))
        if x - 1 >= 0 and len(grid[y][x - 1]) == 0:
            squares.append((y, x - 1))
        if x + 1 < len(grid[0]) and len(grid[y][x + 1]) == 0:
            squares.append((y, x + 1))
        if len(grid[y][x]) == 0:
            squares.append((y, x))
        return squares

    @classmethod
    def search_path(cls, from_y, from_x, to_y, to_x, start_turn):
        q = [(from_y, from_x, start_turn)]
        seen = set()
        seen.add(q[0])
        while q:
            y, x, turn = q.pop(0)
            if y == to_y and x == to_x:
                return turn + 1
            grid = Simulation.get_grid(turn)
            squares = cls.get_movable_squares(y, x, grid)
            for square in squares:
                x = (*square, turn + 1)
                if x not in seen:
                    q.append(x)
                    seen.add(x)


with open("input.txt") as f:
    lines = f.readlines()
Simulation.grid = [
    [[i] if i in "><^v" else [] for i in line.strip()[1:-1]] for line in lines[1:-1]
]
Simulation.get_grid(1)
first = (
    Path.search_path(-1, 0, len(Simulation.grid) - 1, len(Simulation.grid[0]) - 1, 1)
    - 1
)
Simulation.debug(18)
second = (
    Path.search_path(len(Simulation.grid), len(Simulation.grid[0]) - 1, 0, 0, first) - 1
)

last = (
    Path.search_path(
        -1, 0, len(Simulation.grid) - 1, len(Simulation.grid[0]) - 1, second
    )
    - 1
)
print(first, second - first, last - second)
print(last)
