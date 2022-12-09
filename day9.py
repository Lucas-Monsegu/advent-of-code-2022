def is_touching(tx,ty,hx,hy):
    return abs(tx-hx) < 2 and abs(ty-hy) < 2

def move_tail_to_head(tx,ty, hx,hy):

    if is_touching(tx, ty, hx, hy):
        return tx,ty
    nx,ny = tx,ty
    if tx-hx > 1:
        nx -=1
        if ny != hy:
            ny += 1 if ty < hy else -1
    elif hx-tx > 1:
        nx +=1
        if ny != hy:
            ny +=  1 if ty < hy else -1
    elif ty-hy > 1:
        ny -=1
        if nx != hx:
            nx += 1 if tx < hx else -1
    elif hy-ty >1:
        ny +=1
        if nx != hx:
            nx += 1 if tx < hx else -1
    return nx,ny

def move_tails_to_head(tails, hx, hy, tab):
    fx, fy = hx, hy
    for tail in tails:
        tail[0], tail[1] = move_tail_to_head(tail[0], tail[1], fx, fy)
        fx, fy = tail[0], tail[1]
    tab[tails[-1][1]][tails[-1][0]] = 'S'

def print_tab(tails,hx,hy,tab):
    for y in range(len(tab)):
        s=''
        for x in range(len(tab)):
            t = '.'
            for i in range(9):
                if tails[i][0] == x and tails[i][1] == y:
                    t=str(i+1)
            if hx==x and hy==y:
                t = 'H'
            s += t
        print(s)
    print('------------------------------------------------')

with open('input.txt', 'r') as f:
    lines = f.readlines()
    tab_length = 10000
    tab = [['.'for x in range(tab_length)]for i in range(tab_length)]  
    tails = [[len(tab)//2,len(tab)//2] for i in range(9)]
    hx, hy = len(tab)//2,len(tab)//2
    c=0
    for line in lines:
        direction, mag = line.split()
        mag = int(mag)
        if direction == 'R':
            for i in range(hx,hx+mag):
                hx+=1
                move_tails_to_head(tails, hx, hy, tab)
        if direction == 'L':
            for i in range(hx,hx-mag,-1):
                hx-=1
                move_tails_to_head(tails, hx, hy, tab)
        if direction == 'D':
            for i in range(hy,hy+mag):
                hy+=1
                move_tails_to_head(tails, hx, hy, tab)
        if direction =='U':
            for i in range(hy,hy-mag, -1):
                hy-=1
                move_tails_to_head(tails, hx, hy, tab)

        c+=1
    
    # for i in tab : print(''.join(i))

    print(sum(sum(1 if i == 'S' else 0 for i in line)for line in tab))