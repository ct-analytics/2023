import re

with open('day 5/day5.txt', 'r') as f:
    almanac = f.read()

lines = almanac.split('\n\n')
seeds = re.findall(r'\d+', lines[0])
print(seeds)

min_location = float('inf')
for x in map(int, seeds):
    # print(f"Seed: {x}")
    for l in lines[1:]:
        for conversion in re.findall(r'(\d+) (\d+) (\d+)', l):
            destination, source, delta = map(int, conversion)
            
            if x in range(source, source + delta):
                x += destination - source
                break

    # print(f"Location: {x}")
    min_location = min(x, min_location)

print(f"Lowest location is {min_location}")

intervals = []

for seed in re.findall(r'(\d+) (\d+)', lines[0]):
    x1, dx = map(int, seed)
    x2 = x1 + dx
    intervals.append((x1, x2, 1))

min_location = float('inf')
while intervals:
    x1, x2, level = intervals.pop()
    if level == 8:
        min_location = min(x1, min_location)
        continue

    for conversion in re.findall(r'(\d+) (\d+) (\d+)', lines[level]):
        z, y1, dy = map(int, conversion)
        y2 = y1 + dy
        diff = z - y1
        if x2 <= y1 or y2 <= x1:    # no overlap
            continue
        if x1 < y1:                 # split original interval at y1
            intervals.append((x1, y1, level))
            x1 = y1
        if y2 < x2:                 # split original interval at y2
            intervals.append((y2, x2, level))
            x2 = y2
        intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
        break

    else:
        intervals.append((x1, x2, level + 1))

    
print(f"Lowest location is {min_location}")
