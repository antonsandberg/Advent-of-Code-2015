from itertools import cycle, accumulate
from collections import Counter

with open('input.txt') as f:
    data = [x.strip('\n') for x in f.readlines()]

SECONDS = 2503
info = dict()
distances = dict()

for row in data:
    row = row.split()
    info[row[0]] = [int(row[3]), int(row[6]), int(row[13])]
    distances[row[0]] = 0

x = dict()
for name in distances:
    info_list = info[name]
    steps = cycle([info_list[0]]*info_list[1] + [0]*info_list[2])
    distances[name] = list(accumulate(next(steps) for _ in range(2503)))

print(max(h[-1] for h in distances.values()))

scored = [i for a in zip(*distances.values()) for i, v in enumerate(a) if v == max(a)]
by_points = max(Counter(scored).values())
print(by_points)








