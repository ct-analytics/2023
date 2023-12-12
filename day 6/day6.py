import re, math

f = 'day 6/day6.txt'

with open(f, 'r') as input:
    races = input.read()

lines = races.split('\n')
times = [int(x) for x in re.findall(r'\d+', lines[0])]
distances = [int(x) for x in re.findall(r'\d+', lines[1])]
races = list(zip(times,distances))

record = []

for race in races:
    wins = 0
    for t in range(1,race[0]):
        movement = t * (race[0] - t)
        # print(f"{t}: {movement}")
        if movement > race[1]: wins += 1
    
    record.append(wins)
    # print(f"{race}: {wins}")

print(f"Total ways to be the record is: {math.prod(record)}")

race = (int(re.findall(r'\d+', lines[0].replace(" ",""))[0]),
        int(re.findall(r'\d+', lines[1].replace(" ",""))[0]))

min_time = 0
max_time = 0

for t in range(1,race[0]):
    movement = t * (race[0] - t)
    if movement > race[1]: 
        min_time = t
        # print(f"Min @ {t}: {movement}")
        break

for t in range(race[0],1,-1):
    movement = t * (race[0] - t)
    if movement > race[1]: 
        max_time = t
        # print(f"Max @ {t}: {movement}")
        break

print(f"Number of ways to win: {max_time-min_time+1}")