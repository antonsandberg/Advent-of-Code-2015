
def check_validity(x, gates):
    words = x.split(" ")
    if words[1] in ['AND', 'OR']:
        if words[0] and words[2] in gates.keys():
            return True, words[1]
        else:
            try:
                operator_digit = int(words[0])
            except ValueError:
                return False, None
            else:
                return True, words[1] + "_WITH_ONE"
    elif words[0] == 'NOT':
        if words[1] in gates.keys():
            return True, words[0]
    elif words[0] in gates.keys():
        return True, words[1]
    else:
        try:
            addable_digit = int(words[0])
        except ValueError:
            return False, None
        else:
            return True, 'ADD'
    return False, None


with open('input.txt') as f:
    data = f.readlines()
data = [line.strip() for line in data]

gates = dict()

for instruction in data:
    words = instruction.split()
    validity, operation = check_validity(instruction, gates)
    if not validity:
        pass

    if operation == 'ADD':
        gates[words[2]] = int(words[0])
    else:
        if operation == 'AND':
            print('And')
            gates[words[-1]] = gates[words[0]] & gates[words[2]]
        elif operation == 'OR':
            print('Or')
            gates[words[-1]] = gates[words[0]] | gates[words[2]]
        elif operation == 'RSHIFT':
            print('R')
            gates[words[-1]] = gates[words[0]] >> int(words[2])
        elif operation == 'LSHIFT':
            print('L')
            gates[words[-1]] = gates[words[0]] << int(words[2])
        elif operation == 'NOT':
            print('Not')
            gates[words[-1]] = ~ gates[words[1]]
        elif operation == 'ADD_WITH_ONE':
            gates[words[-1]] = 1 & gates[words[2]]
        elif operation == 'OR_WITH_ONE':
            gates[words[-1]] = 1 | gates[words[2]]



print(gates['a'])
