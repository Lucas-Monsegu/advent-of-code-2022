with open('input.txt', 'r') as f:
    lines = f.readlines()

    elves = []    
    calories = 0
    for line in lines:
        if len(line) == 1:
            elves += [calories]
            calories = 0
        else:
            calories += int(line)
    t = 0
    for i in range(3):
        for i,elve in enumerate(elves):
            if elve == max(elves):
                t+=elves.pop(i)
                break
            
    print(t)