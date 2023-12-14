import re, math
from pprint import pprint

f = 'day 8/day8.txt'

with open(f,'r') as input:
    lines = input.read().split('\n')

instructions = lines[0]

network = dict()

for l in lines[2:]:
    n = re.findall(r'(\w+)',l)
    network[n[0]] = {'L':n[1],'R':n[2]}

def get_steps(network=network,instructions=instructions,next_node='AAA',part1=True):
    
    steps = 0
    i = 0
    while True:
        if i >= len(instructions): i = 0

        d = instructions[i]
        next_node = network[next_node][d]
        steps +=1
        i += 1
        
        if part1 and next_node == 'ZZZ': break
        if not part1 and next_node[2] == 'Z':break 

    return steps

print(f'Part 1: Number of steps: {get_steps(next_node="AAA")}')

starting_nodes = [x for x in network.keys() if x[2]=='A']

part2_steps = [get_steps(next_node=n,part1=False) for n in starting_nodes]

print(f'Part 2: Number of steps: {math.lcm(*part2_steps)}')