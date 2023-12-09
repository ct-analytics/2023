import re

f = "day 2/day2.txt"
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
game_number = re.compile(r'Game\s(\d+): ')
b = re.compile(r' (\d+) (blue|green|red)')
# ?:\s(?:\d+\s(blue|green|red))+;

def check(maxes,d={'red': 12, 'green':13, 'blue':14}):
    c = True
    # print(maxes)
    for k,v in maxes.items():
        if d[k]<v:
            c = False

    return(c)

all_games = []

with open(f,'r') as games:
    for i, l in enumerate(games):
        # print(f"{i}: {l}")
        s = re.split(r'Game (\d+):',l)
        # print(f"{i}: {s}")
        g = [x.split(";") for x in s]

        game = {'number': int(g[1][0]), 'cube_sets': g[2]}
        # print(f"{i}: {game}")
        # print(game['cube_sets'])
        
        e = [p.split(",") for p in g[2]]
        # print(e)

        b2 = [b.findall(y) for x in e for y in x]
        # print(b2)
        b3 = [(x[0][1],int(x[0][0])) for x in b2]
        # print(b3)
        b4 = dict()
        for k,v in b3:
            b4.setdefault(k, []).append(v)
        
        # print(b4)

        game['cube_maxes'] = {k:max(v) for k,v in b4.items()}
        # print(f"{i}: {game}")

        game['check'] = check(game['cube_maxes'])
        # print(f"{i}: {game}")

        all_games.append(game)

# print(all_games)
print(f"Number of games that are possible: {sum(1 for g in all_games if g['check'])}")
print(f"Sum of IDs: {sum(g['number'] for g in all_games if g['check'])}")
