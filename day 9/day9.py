import math
from pprint import pprint

f = 'day 9/day9.txt'

def diffs(l):
    d = []
    for i in range(len(l)-1):
        d.append(l[i+1]-l[i])

    # print(d)
    return d

with open(f,'r') as input:
    extrapolated_values = []
    for i, line in enumerate(input):
        readings = [int(x) for x in line.strip().split(" ")]
        # print(readings)

        d = list()
        d.append(readings)
        
        i = 0
        while sum(d[i]) != 0:
            i+=1
            d.append(diffs(d[i-1]))

        s = sum([x[-1] for x in d])
        # pprint(d)
        print(f"Next value is: {s}")
        extrapolated_values.append(sum([x[-1] for x in d]))

# print(extrapolated_values)
print(f"Sum of extrapolated values: {sum(extrapolated_values)-1}")
# 1856890045 too high
# 1853145120 too high
# 1853145119