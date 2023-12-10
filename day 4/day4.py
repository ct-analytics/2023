import re
from collections import Counter

f = 'day 4/day4.txt'

all_cards = []
card_counter = Counter()

with open(f,'r') as scratchcards:
    for i, l in enumerate(scratchcards):
        s = re.split(r'Card\s+(\d+):',l)
        c = [x.split("|") for x in s]
        
        card = {'n': int(c[1][0]), 'numbers': c[2]}
        card_counter.update([card['n']])
        
        card['winning numbers'] = set([int(x) for x in card['numbers'][0].strip().split(' ') if x != ''])
        card['elf numbers'] = set([int(x) for x in card['numbers'][1].strip().split(' ') if x != ''])
        card['intersection'] = card['winning numbers'].intersection(card['elf numbers'])
        card['len of intersection'] = len(card['intersection'])
        for c in range(card_counter[card['n']]):
            card_counter.update([x+card['n']+1 for x in range(card['len of intersection'])])

        if card['len of intersection'] > 0:
            card['score'] = 2**(card['len of intersection']-1)
        else:
            card['score'] = 0
        
        all_cards.append(card)
        

print(f"Point total: {sum(card['score'] for card in all_cards)}")
print(f"Total cards won: {sum(card_counter.values())}")