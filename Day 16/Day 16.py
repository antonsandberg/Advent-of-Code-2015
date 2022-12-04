import re

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

targets = {'children:': 3,
'cats:': 7,
'samoyeds:': 2,
'pomeranians:': 3,
'akitas:': 0,
'vizslas:': 0,
'goldfish:': 5,
'trees:': 3,
'cars:': 2,
'perfumes:': 1}

for i, row in enumerate(data):
    _, _, thing_1, thing_1_num, thing_2, thing_2_num, thing_3, thing_3_num = row.split()
    things_dict = dict()
    things_dict[thing_1] = int(thing_1_num.strip(','))
    things_dict[thing_2] = int(thing_2_num.strip(','))
    things_dict[thing_3] = int(thing_3_num.strip(','))

    conds = []
    for key, value in things_dict.items():
        if key in ['cats:', 'trees:']:
            conds.append(value > targets[key])
        elif key in ['pomeranians:', 'goldfish:']:
            conds.append(value < targets[key])
        else:
            conds.append(value == targets[key])

    if all(conds):
        print(i+1)
        break








