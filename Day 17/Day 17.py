import itertools

# ? blabla
# ! bla bla
#TODO: asdfasdfasdf

with open('input.txt') as f:
    data = [int(x) for x in f.read().split()]

total_sum = 0
for i in range(len(data)-1):
    combs = itertools.combinations(data, i)
    valid_combs = [1 for x in combs if sum(x) == 150]
    total_sum += len(valid_combs)
    if total_sum != 0:
        print(i)
        break

print(total_sum)
