from collections import Counter
from functools import cmp_to_key
from pprint import pprint

f = 'day 7/day7.txt'

with open(f,'r') as input:
    lines = input.read()

games = [x.split(" ") for x in lines.split('\n')]
hands = list()

for n,g in enumerate(games):
    hands.append({'n': n+1, 'hand':g[0], 'bid': int(g[1])})

# print(hands)

def type(hand):
    # 7: Five of a kind, where all five cards have the same label: AAAAA
    # 6: Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # 5: Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # 4: Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # 3: Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # 2: One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # 1: High card, where all cards' labels are distinct: 23456

    c = Counter(hand)
    if 5 in c.values(): return 7
    if 4 in c.values(): return 6
    if 3 in c.values() and 2 in c.values(): return 5
    if 3 in c.values(): return 4
    if 2 in Counter(c.values()).values(): return 3
    if 2 in c.values(): return 2
    return 1

def type_part2(hand):
    # 7: Five of a kind, where all five cards have the same label: AAAAA
    # 6: Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # 5: Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # 4: Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # 3: Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # 2: One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # 1: High card, where all cards' labels are distinct: 23456

    # score = 1
    j = hand.count('J')
    h = [card for card in hand if card != 'J']
    c = Counter(h)
    counts = sorted(c.values(), reverse=True)
    if not counts:
        counts = [0]
    if counts[0] + j == 5:
        return 6
    if counts[0] + j == 4:
        return 5
    if counts[0] + j == 3 and counts[1] == 2:
        return 4
    if counts[0] + j == 3:
        return 3
    if counts[0] == 2 and (j or counts[1] == 2):
        return 2
    if counts[0] == 2 or j:
        return 1
    return 0

def compare_hands(h1,h2):
    d = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2': 1}
    if h1['type'] == h2['type']:
        for i in range(5):
            if d[h1['hand'][i]] > d[h2['hand'][i]]: return 1
            if d[h1['hand'][i]] < d[h2['hand'][i]]: return -1
            if d[h1['hand'][i]] == d[h2['hand'][i]]: continue

        return 0
    if h1['type'] > h2['type']: return 1
    if h1['type'] < h2['type']: return -1
    return 0

def compare_hands_part2(h1,h2):
    d = {'A':13, 'K':12, 'Q':11, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2': 2}
    if h1['type'] == h2['type']:
        for i in range(5):
            if d[h1['hand'][i]] > d[h2['hand'][i]]: return 1
            if d[h1['hand'][i]] < d[h2['hand'][i]]: return -1
            if d[h1['hand'][i]] == d[h2['hand'][i]]: continue

        return 0
    if h1['type'] > h2['type']: return 1
    if h1['type'] < h2['type']: return -1
    return 0

for h in hands:
    h['type'] = type(h['hand'])
    # print(f"{h['n']}: {h['hand']} is type {h['type']}.")

# print("****************")
# pprint(hands)
hands_sorted = sorted(hands, key=cmp_to_key(compare_hands), reverse=False)
# print("****************")
# pprint(hands_sorted)

for r,h in enumerate(hands_sorted):
    h['rank'] = r+1

# print("****************")
# pprint(hands_sorted)
print(f"Part 1: Winnings: {sum([h['bid'] * h['rank'] for h in hands_sorted])}")

for h in hands:
    h['type'] = type_part2(h['hand'])
    # print(f"{h['n']}: {h['hand']} is type {h['type']}.")

# print("****************")
# pprint(hands)
hands_sorted = sorted(hands, key=cmp_to_key(compare_hands_part2), reverse=False)
# print("****************")
# pprint(hands_sorted)

for r,h in enumerate(hands_sorted):
    h['rank'] = r+1

# print("****************")
# pprint(hands_sorted)

print(f"Part 2: Winnings: {sum([h['bid'] * h['rank'] for h in hands_sorted])}")
