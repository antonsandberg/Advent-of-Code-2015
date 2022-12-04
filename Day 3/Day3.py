
def present_delivery(move, visited, presents, current_position):
    y, x = current_position
    if move == 'v':
        y += -1
    elif move == '^':
        y += 1
    elif move == '>':
        x += 1
    elif move == '<':
        x += -1
    if (y, x) not in visited:
        visited.add((y, x))
        presents[(y, x)] = 1
    else:
        presents[(y, x)] += 1
    return visited, presents, (y, x)


with open('input.txt') as f:
    data = [x for x in f.read().strip()]

visited = set()
presents = dict()
santa_position = (0, 0)
helper_position = (-1, 0)
presents[(-1, 0)] = 1
#visited.add((-1, 0))

for i, move in enumerate(data[1:-1]):
    if i % 2 == 0:
        visited, presents, santa_position = present_delivery(move, visited, presents, santa_position)
    else:
        visited, presents, helper_position = present_delivery(move, visited, presents, helper_position)

present_counts = presents.values()
good_houses = len([x for x in present_counts if x >= 1])
print(good_houses)