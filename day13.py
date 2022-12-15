from functools import cmp_to_key


def cmp(list1, list2):
    print('in cmp', list1,list2)
    def rec(l1, l2):
        for i in range(len(l1)):
            n1 = l1[i]
            if len(l2) <= i:
                return False
            n2 = l2[i]
            r = -1
            if type(n1) == list:
                if type(n2) != list:
                    n2 = [n2]
                r = rec(n1,n2) 
            elif type(n2) == list:
                if type(n1) != list:
                    n1 = [n1]
                r = rec(n1,n2)
            if r == None:
                continue
            elif r == True or r == False:
                return r
            if n1 < n2:
                return True
            if n1 > n2:
                return False
        if len(l1) < len(l2):
            return True
        return None
            
    r = rec(list1, list2)
    if r is None:
        return 0
    if r is True:
        return -1
    if r is False:
        return 1

with open('input.txt') as f:
    lines = f.readlines()

packets = []
for line in lines:
    if len(line) < 2: continue
    packets += [eval(line)]


packets.append([[2]])
packets.append([[6]])
print(packets)
l = list(sorted(packets, key=cmp_to_key(cmp)))
print((l.index([[2]])+1) * (l.index([[6]])+1) )