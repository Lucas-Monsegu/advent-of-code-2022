t = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}
with open('input.txt', 'r') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        a,b = line.split()
        a = t[a]
        if b == 'X':
            b = a-1 if a-1 > 0 else 3
        if b == 'Y':
            b = a
        if b == 'Z':
            b = a+1 if a+1 <= 3 else 1

        dif = b-a
        if dif == -2:
            total += 6
        if dif == 2:
            total += 0
        elif  dif > 0:
            total += 6
        elif dif == 0:
            total += 3
        else:
            total += 0
        total += b
    print(total)