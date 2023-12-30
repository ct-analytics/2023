import math
from pprint import pprint

f = 'day 9/day9.txt'

def get_value(h,pos):
    if all(n==0 for n in h):
        return 0
    else:
        diff = [h[i+1] - h[i] for i in range(len(h)-1)]
        if pos=="next":
            return h[-1] + get_value(diff,"next")
        elif pos=="prev":
            return h[0] - get_value(diff,"prev")

with open(f,'r') as input:
    next_values = []
    previous_values = []

    for i, line in enumerate(input):
        readings = [int(x) for x in line.strip().split(" ")]

        previous_values.append(get_value(readings,"prev"))
        next_values.append(get_value(readings,"next"))

print(f"Part 1: Sum of extrapolated values: {sum(next_values)}")
print(f"Part 2: Sum of extrapolated values: {sum(previous_values)}")
