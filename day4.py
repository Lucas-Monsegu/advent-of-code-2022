with open('input.txt', 'r') as f:
    lines = f.readlines()
    c=0
    for line in lines:
        s1,s2 = line.split(',')
        s1 = list(map(int,s1.split('-')))
        s2 = list(map(int, s2.split('-')))
        
        if s1[0] <= s2[1] and s1[1] >= s2[0]:
            c+=1
        elif s2[1] <= s1[0] and s2[1] >= s1[0]:
            c+=1
    print(c)            