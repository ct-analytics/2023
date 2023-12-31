import math
from pprint import pprint
from itertools import combinations

f = "day 11/day11.txt"

with open(f,'r') as input:
    galaxy = [[x for x in row] for row in input.read().strip().split('\n')]

print("Raw input:")
pprint(galaxy)

def check_empty(g,transpose=False):
    if transpose:
        g = [list(a) for a in zip(*g)]

    empty_rows = list()
    row_to_insert = ["." for x in range(len(g[0]))]
    for i,row in enumerate(g):
        if all(r == "." for r in row):
            empty_rows.append(i + len(empty_rows))

    for r in empty_rows:
        g.insert(r,row_to_insert)

    if transpose:
        print(f"Adding {len(empty_rows)} cols.")
        g = [list(a) for a in zip(*g)]
    else:
        print(f"Adding {len(empty_rows)} rows.")
    
    return g

# print("################################")
# pprint(check_empty(galaxy))
# print("################################")
# pprint(check_empty(galaxy,transpose=True))
# print("################################")

galaxy = check_empty(galaxy)
galaxy = check_empty(galaxy,transpose=True)

galaxies = dict()
# galaxies = list()
n_galaxies = 1
print("Expanded galaxy:")
pprint(galaxy)

for i,row in enumerate(galaxy):
    for j,col in enumerate(row):
        pos = (i+1,j+1)
        if col == "#":
            galaxies[n_galaxies] = pos
            # galaxies.append(pos)
            n_galaxies += 1

pprint(galaxies)
c = combinations(galaxies.items(),2)
# c = combinations(galaxies,2)

def dist(combo):
    # print(combo)
    g1=combo[0]
    g2=combo[1]
    # print(f"Distance is ({g1[1][0]}-{g2[1][0]}) + ({g1[1][1]}-{g2[1][1]})")
    d = abs(g1[1][0]-g2[1][0]) + abs(g1[1][1]-g2[1][1])

    return d

shortest_path_sum = 0
for i in c:
    print(f"Galaxies {i[0][0]} at {i[0][1]} and {i[1][0]} at {i[1][1]} are {dist(i)} steps apart.")
    shortest_path_sum += dist(i)

print(f"Sum of the shortest path between all pairs of galaxies is {shortest_path_sum}.")