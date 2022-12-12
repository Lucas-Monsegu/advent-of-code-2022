def add_one_to_clock(clock, value,pixels):
    char = '.'
    if (clock % 40) in [value-1, value,value+1]:
        char = '#'    
    if clock >= 240:
        return
    pixels[clock//40] += char
    clock += 1

    return clock


with open('input.txt') as f:
    lines = f.readlines()
    clock = 0
    value = 1
    pixels = [[]for i in range(6)]
    for line in lines:
        if 'noop' in line:
            clock = add_one_to_clock(clock, value, pixels)
        else:
            _,v = line.split()
            v = int(v)
            clock = add_one_to_clock(clock, value, pixels)
            clock = add_one_to_clock(clock, value, pixels)
            value += v

    for pixel in pixels: print(''.join(pixel))