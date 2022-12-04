from itertools import groupby

with open('input.txt') as f:
    data = f.read().strip()

a = groupby(data)
print(list(list(a)[3][1]))



