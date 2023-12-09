import re
import math

f = "day 2/day2.txt"
game_number = re.compile(r'Game\s(\d+): ')
b = re.compile(r' (\d+) (blue|green|red)')

def check(maxes,d={'red': 12, 'green':13, 'blue':14}):
    c = True
    for k,v in maxes.items():
        if d[k]<v:
            c = False

    return(c)

all_games = []

with open(f,'r') as games:
    for i, l in enumerate(games):
        s = re.split(r'Game (\d+):',l)
        g = [x.split(";") for x in s]

        game = {'number': int(g[1][0]), 'cube_sets': g[2]}
        
        e = [p.split(",") for p in g[2]]

        b2 = [b.findall(y) for x in e for y in x]
        b3 = [(x[0][1],int(x[0][0])) for x in b2]
        b4 = dict()
        for k,v in b3:
            b4.setdefault(k, []).append(v)

        game['cube_maxes'] = {k:max(v) for k,v in b4.items()}

        game['check'] = check(game['cube_maxes'])

        game['power'] = math.prod([v for k,v in game['cube_maxes'].items()])

        all_games.append(game)

print(f"Number of games that are possible: {sum(1 for g in all_games if g['check'])}")
print(f"Sum of IDs: {sum(g['number'] for g in all_games if g['check'])}")

print(f"Sum of the power of these sets: {sum(g['power'] for g in all_games)}")
