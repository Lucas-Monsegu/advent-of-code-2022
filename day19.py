from copy import copy


def simulate_bp(blueprint):
    def rec(ressources, robots, minute):
        global debug

        if minute == 33:
            return ressources['geode']
        
        univer = 0
        if ressources['ore'] >= blueprint['clay'][0] and ressources['ore'] - robots['ore'] < blueprint['clay'][0] and robots['clay'] < max_clay:
            re, ro = copy(ressources), copy(robots)
            re['ore'] -= blueprint['clay'][0]
            ro['clay'] += 1
            for robot in robots: re[robot] += robots[robot]
            univer = rec(re, ro, minute+1)
        if ressources['ore'] >= blueprint['ore'][0] and ressources['ore'] - robots['ore'] < blueprint['ore'][0]  and  robots['ore'] < max_ore:
            re, ro = copy(ressources), copy(robots)
            re['ore'] -= blueprint['ore'][0]
            ro['ore'] += 1
            for robot in robots: re[robot] += robots[robot]
            univer = max(univer, rec(re, ro, minute+1))
        if ressources['ore'] >= blueprint['obsidian'][0] and ressources['clay'] >= blueprint['obsidian'][1] and robots['obsidian'] < max_obsdian:
            re, ro = copy(ressources), copy(robots)
            re['ore'] -= blueprint['obsidian'][0]
            re['clay'] -= blueprint['obsidian'][1]
            ro['obsidian'] += 1
            for robot in robots: re[robot] += robots[robot]
            univer = max(univer, rec(re, ro, minute+1 ))
        if ressources['ore'] >= blueprint['geode'][0] and ressources['obsidian'] >= blueprint['geode'][1]:
            re, ro = copy(ressources), copy(robots)
            re['ore'] -= blueprint['geode'][0]
            re['obsidian'] -= blueprint['geode'][1]
            ro['geode'] += 1
            for robot in robots: re[robot] += robots[robot]
            univer = max(univer, rec(re, ro, minute+1))
            return univer
        for robot in robots: ressources[robot] += robots[robot]
        return max(univer, rec(ressources, robots, minute+1))


    ressources = {
        'ore': 0,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }
    robots = {
        'ore': 1,
        'clay': 0,
        'obsidian': 0,
        'geode': 0, 
    }
    max_obsdian = blueprint['geode'][1]
    max_clay = blueprint['obsidian'][1]
    max_ore = max(blueprint['ore'][0], blueprint['clay'][0], blueprint['obsidian'][0], blueprint['geode'][0])
    print(max_clay, max_clay, max_ore)

    return rec(ressources, robots, 1)
    


with open('input.txt') as f:
    lines = f.readlines()

blueprints = []
for line in lines:
    phrases = line.split(':')[1]
    costs = list(map(int, [i for i in phrases.split() if i.isnumeric()]))
    ore_robot, clay_robot, obsidian_robot, goeode_robot = [(costs[0],), (costs[1],), (costs[2], costs[3]), (costs[4], costs[5])]
    blueprints.append({
        'ore': ore_robot,
        'clay': clay_robot,
        'obsidian': obsidian_robot,
        'geode': goeode_robot
    })
m = 0
mi = 0
x = 0
for i,bp in enumerate(blueprints):
    s = simulate_bp(bp)
    print(s,'*', (i+1))
    x += s *  (i+1)
print(x)