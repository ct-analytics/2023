import re
from pprint import pprint

f = 'day 8/day8.txt'

with open(f,'r') as input:
    lines = input.read().split('\n')

instructions = lines[0]

network = dict()

for l in lines[2:]:
    # print(l)
    n = re.findall(r'(\w+)',l)
    # print(n)
    network[n[0]] = {'L':n[1],'R':n[2]}

pprint(instructions)
pprint(network)

next_node = 'AAA'
steps = 0
i = 0
while True:
    # if i == 0:
    #     next_node = network['AAA'][d]
    # else: 
    #     next_node = network[next_node][d]
    if i >= len(instructions): i = 0

    d = instructions[i]
    next_node = network[next_node][d]
    # print(i)
    steps +=1
    i += 1
    
    if next_node == 'ZZZ': break

print(f'Number of steps: {steps}')
