import re
import json


def sum_numbers(s):
    return sum(int(i) for i in re.findall(r"(-?\d+)", str(s)))


def sum_numbers_2(s):
    if type(s) is str:
        return 0
    if type(s) in [int, float]:
        return s
    if type(s) is dict:
        if 'red' in list(s.values()):
            return 0
        s = list(s.values())
    if type(s) is list:
        return sum(map(sum_numbers_2, s))
    raise ValueError(type(s))



def main():
    with open('input.txt') as f:
        data = json.loads(f.read())

    print(sum_numbers(data))
    print(sum_numbers_2(data))


if __name__ == '__main__':
    main()


