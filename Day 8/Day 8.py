

with open('Day 8/input.txt') as f:
    data = f.read().split()

string_lengths = 0
memory_amount = 0
string_lengths_2 = 0
for input in data:
    string_lengths += len(input)
    memory_amount += len(eval(input))
    string_lengths_2 += 2+input.count('\\') + input.count('"')


print(string_lengths - memory_amount)
print(string_lengths_2)


