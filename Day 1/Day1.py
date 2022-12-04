with open('input.txt') as f:
    data = f.read().strip()

floor = 0
for i, symbol in enumerate(data):
    if symbol == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i+1)
print(floor)