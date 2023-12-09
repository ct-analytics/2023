import math
import re

f = 'day 3/day3.txt'

s = dict()
schematic = list(open(f,'r'))
h = len(schematic)
w = len(schematic[0])

symbols = {(row,col): [] for row in range(h) for col in range(w-1) if schematic[row][col] not in '.1234567890'}
gears = {(row,col): [] for row in range(h) for col in range(w-1) if schematic[row][col]=="*"}

for i,row in enumerate(schematic):
    for j in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (i-1, i, i+1)
                       for c in range(j.start()-1, j.end()+1)}
                
        for k in edge & symbols.keys():
            symbols[k].append(int(j.group()))

        for k in edge & gears.keys():
            gears[k].append(int(j.group()))    


print(f'Sum of part numbers: {sum(sum(part) for part in symbols.values())}')
print(f'Product of part numbers: {sum(math.prod(part) for part in gears.values() if len(part)==2)}')
