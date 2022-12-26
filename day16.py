
from collections import defaultdict
from functools import cache


class Valve:
    def __init__(self, name, flow_rate):
        self.flow_rate = int(flow_rate)
        self.name = name
        self.tunnels = []
        self.seen = False
        self.openend = False
        self.value = 100000


    def reset(self):
        self.seen = False

    def __hash__(self):
        return str.__hash__(self.name)
    
    def __lt__(self, other):
        return self.flow_rate < other.flow_rate

class Preprocess:
    def __init__(self, valves):
        self.valves = valves
        # self.distance_field = {
        #     valve:{} for valve in valves #if valve.flow_rate > 0
        # }
        pass
        # print(self.positif_flow_valves)
        # self.distance_field[valves[0]] = {v:self.dijkstra_min_dist(valves[0], v) for v in filter(lambda x: x != valve and x.flow_rate > 0, valves)}
        # self.distance_field[valves[0]] = {valves[3]:1}
        # self.distance_field[valves[3]] = {valves[1]:2}
        # self.distance_field[valves[1]] = {valves[9]:3}
        # self.distance_field[valves[9]] = {valves[7]:7}
        # self.distance_field[valves[7]] = {valves[4]:3}
        # self.distance_field[valves[4]] = {valves[2]:2}

    def dijkstra_min_dist(self, start, end):
        q = []
        q.append(start)
        q[0].value = 0
        while len(q) > 0:
            v = q.pop(0)
            if v.seen:
                continue
            v.seen =True
            for n in v.tunnels:
                if v.value + 1 < n.value:
                    n.value = v.value + 1
            q += (list(i for i in v.tunnels if not i.seen))
            q.sort(key=lambda x: x.value)
        r = end.value
        for v in self.valves:v.seen,v.value = False, 100000
        return r

class Compute:
    def maximize_flow(self, start):
        
        distance_field =defaultdict(dict)
        for valve in valves:
            # if valve.flow_rate >0:
            distance_field[valve.name] = {
                v.name:Preprocess(valves).dijkstra_min_dist(valve, v) for v in  filter(lambda x:  x.flow_rate > 0, valves) 
            }
        positif_flow_valves = {v.name: v.flow_rate for v in valves if v.flow_rate > 0}
        def rec(me, elephant, seen_valves):
            r = 0
            for valv, flow_rate in positif_flow_valves.items():
                if valv in seen_valves:
                    continue
                
                current_seen_valves = tuple(sorted([*seen_valves, valv]))
                valv1, clock1 = me
                if valv in distance_field[valv1] and clock1 - distance_field[valv1][valv] >= 1:
                    new_clock_1 = clock1 - distance_field[valv1][valv] -1
                    my_move = rec((valv, new_clock_1), elephant, current_seen_valves) + new_clock_1 * flow_rate
                    r = max(r, my_move )

                valv2, clock2 = elephant
                if valv in distance_field[valv2] and clock2 - distance_field[valv2][valv] >= 1:
                    new_clock_2 = clock2 - distance_field[valv2][valv] -1
                    elephant_move = rec(me, (valv, new_clock_2), current_seen_valves) +new_clock_2 * flow_rate
                    r = max(r, elephant_move )
            return r
            
        return rec(("AA", 26), ("AA", 26), ())

valves = []
tunnels = {}
with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    l = line.replace(';', '').replace(',', '').split()
    name = l[1]
    rate = l[4].split('=')[1]
    tunnel = l[8:]
    valves.append(Valve(name, rate))
    tunnels[name] = tunnel

for valve in valves:
    valve.tunnels = list(filter(lambda v: v.name in tunnels[valve.name], valves)) 

valves.sort(key=lambda x: x.name)
start = valves[0]
# preprocess = Preprocess(valves)
print(Compute().maximize_flow(start))
# opened_valves = []
# for turn in range(30):
#     print(f'== Minute {turn+1} ==')
#     print(f'Opened valves({len(opened_valves)}): ', *[x.name for x in opened_valves], 'pressure:', sum(x.flow_rate for x in opened_valves))
#     print(get_max_pressure_gain(valves, turn))
#     print()