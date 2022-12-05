with open('input.txt', 'r') as f:
    lines = f.readlines()
    t = 0
    ruck = []
    for line in lines:
        ruck += [line]
        print(ruck)
        if len(ruck) == 3:
            for i in ruck[0]:
                print(i)
                if all (i in x for x in ruck):
                    letter = i
                    break
            ruck = []
        
            if letter.isupper():
                t+= ord(letter)-ord('A')+27
            else:
                t+=ord(letter)-ord('a')+1
    print(t)