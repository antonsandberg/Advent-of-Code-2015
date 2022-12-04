from itertools import permutations

with open('input.txt') as f:
    data1 = [x.strip() for x in f.readlines()]

guests = set()
for sentence in data1:
    person1, _, operation, value, _, _, _, _, _, _, person2 = sentence.split()
    for person in [person1, person2]:
        guests.add(person.strip('.'))

interactions = dict()

guests.add('Anton')
combinations = permutations(list(guests))

for sentence in data1:
    person1, _, operation, value, _, _, _, _, _, _, person2 = sentence.split()
    person2 = person2.strip('.')
    key = f'{person1} next to {person2}'
    if 'Anton' in [person1, person2]:
        continue
    if operation == 'gain':
        interactions[key] = int(value)
    else:
        interactions[key] = -int(value)

current_best = 0
for seating in combinations:
    this_round = 0
    for i, person in enumerate(seating):
        if i == 0:
            left = seating[-1]
            right = seating[i+1]
        elif i == len(seating)-1:
            left = seating[i-1]
            right = seating[0]
        else:
            left = seating[i-1]
            right = seating[i+1]
        if person == 'Anton':
            continue
        for neighbor in [left, right]:
            if neighbor == 'Anton':
                continue
            key = f'{person} next to {neighbor}'
            this_round += int(interactions[key])
    current_best = max(this_round, current_best)

print(current_best)
