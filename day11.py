from math import gcd


class Monkey:
    def __init__(self, name, items, op, test, true, false):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.true = true
        self.false = false
        self.activity = 0
    
    def play_turn(self, monkeys, prime_product):
        for item in self.items:
            new_item = self.op(item) % prime_product
            self.activity += 1
            d = gcd(new_item, self.test)
            if new_item % self.test == 0:
                monkeys[self.true].items.append(new_item)
            else:
                monkeys[self.false].items.append(new_item)
        self.items = []

    def __repr__(self):
        return f'Monkey {self.name}: inspected items: {self.activity} times'


with open('input.txt') as f:
    lines = f.readlines()

monkeys = []    
for i in range(0,len(lines), 7):
    name = next(filter(lambda x: x.isnumeric(), lines[i]))
    items = eval(f'[{lines[i+1].split(":")[1]}]')
    op = eval(f'lambda old: {lines[i+2].split("new = ")[1]}')
    test= int(lines[i+3].split("by")[1].strip())
    true = int(lines[i+4].split('to monkey')[1])
    false = int(lines[i+5].split('to monkey')[1])
    monkeys += [Monkey(name, items, op, test, true, false)]

prime_product = eval('*'.join(str(m.test) for m in monkeys))
for turn in range(10000):
    for monkey in monkeys:
        monkey.play_turn(monkeys, prime_product)
    print('round', turn+1)
    # for monkey in monkeys: print(f'{monkey.name} {monkey.items}')

m1 = max(monkeys, key=lambda m: m.activity)
monkeys.remove(m1)
m2 = max(monkeys, key=lambda m: m.activity)
print(m1.activity * m2.activity)