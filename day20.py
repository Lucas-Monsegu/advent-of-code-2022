from collections import deque

with open('input.txt') as f:
    lines = f.readlines()

data = list(map(lambda x: int(x)* 811589153, lines))

q = deque([(x, i )for i, x in enumerate(data)])

for i in range(10):
    for i, v in enumerate(data):
        pos = q.index((v,i))
        q.rotate(-pos)
        q.popleft()
        q.rotate(-v)
        q.appendleft((v,i))

res = [i[0] for i in q]
index_0 = res.index(0)
vals = [res[(index_0 + i) % len(data)] for i in [1000,2000,3000]]
print(vals)
print(sum(vals))