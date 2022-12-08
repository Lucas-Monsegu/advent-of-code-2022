with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        unique_chars = []
        for i in range(len(line)):
            unique_chars.append(line[i])
            if len(set(unique_chars)) == 14:
                print(i+1, unique_chars)
                break
            elif(i>=13):
                unique_chars.pop(0)