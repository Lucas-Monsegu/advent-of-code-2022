with open('input.txt') as f: lines = f.readlines()

monkeys = {line[0]:line[1] for line in map(lambda x: x.split(':'),lines)}
for monkey in monkeys: 
    if monkeys[monkey].strip().isnumeric():
        monkeys[monkey] = int(monkeys[monkey].strip())


def calculate(monkeys, name, test=None):
    def rec(monkey,test=None):
        val = monkeys[monkey]
        if monkey == 'humn':
            if test: return test 
            return 3330805295851
        if type(val) == int: return val
       
        if '*' in val:
            m1, m2 = list(map(lambda x:x.strip(), val.split('*')))
            r1, r2 = rec(m1, test), rec(m2, test)
            if r1 is None or r2 is None: return None
            return r1 * r2

        if '/' in val:
            m1, m2 = list(map(lambda x:x.strip(), val.split('/')))
            r1, r2 = rec(m1, test), rec(m2, test)
            if r1 is None or r2 is None: return None
            return r1 // r2

        if '+' in val:
            m1, m2 = list(map(lambda x:x.strip(), val.split('+')))
            r1, r2 = rec(m1, test), rec(m2, test)
            if r1 is None or r2 is None: return None
            return r1 + r2

        if '-' in val:
            m1, m2 = list(map(lambda x:x.strip(), val.split('-')))
            r1, r2 = rec(m1, test), rec(m2, test)
            if r1 is None or r2 is None: return None
            return r1 - r2

    return rec(name,test)

def smart_brute_force(monkeys, monkey, to_find):
    import time
    window = [0,145167969204648]
    while True:
        test = window[0] + abs(window[1]-window[0]) // 2
        r = calculate(monkeys, monkey, test)
        if r > to_find:
            window[0] = test
        if r < to_find:
            window[1] = test
        if r == to_find:
            return test
        print(window)
        time.sleep(0.2)

a,b = list(map(lambda x: x.strip(), monkeys['root'].split('+')))

monkeys['root'] = monkeys['root'].replace('+', '-')
print(smart_brute_force(monkeys, 'root', 0))