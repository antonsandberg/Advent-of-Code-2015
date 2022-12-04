import numpy as np


def extract_start_n_end(s):
    if s[0] == 'toggle':
        s_numbers = s[1].split(',')
        e_numbers = s[3].split(',')
        s_x, s_y = int(s_numbers[0]), int(s_numbers[1])
        e_x, e_y = int(e_numbers[0]), int(e_numbers[1])
    else:
        s_numbers = s[2].split(',')
        e_numbers = s[4].split(',')
        s_x, s_y = int(s_numbers[0]), int(s_numbers[1])
        e_x, e_y = int(e_numbers[0]), int(e_numbers[1])
    return s_y, e_y, s_x, e_x


def main():
    with open('input.txt') as f:
        data = [line.strip().split() for line in f.readlines()]

    N = 1000
    lamps = np.zeros((N, N))

    for instr in data:
        start_y, end_y, start_x, end_x = extract_start_n_end(instr)
        if instr[0] == 'turn':
            if instr[1] == 'off':
                lamps[start_y:end_y+1, start_x:end_x+1] -= 1
                lamps[lamps < 0] = 0
            else:
                lamps[start_y:end_y+1, start_x:end_x+1] += 1

        else:
            lamps[start_y:end_y+1, start_x:end_x+1] += 2
            # lamps[start_y:end_y+1, start_x:end_x+1] = lamps[start_y:end_y+1, start_x:end_x+1] % 2

    # n_lamps_on = len(lamps[lamps == 1])
    sum_lights_on = sum(sum(lamps))
    # print(n_lamps_on)
    print(sum_lights_on)


if __name__ == '__main__':
    main()
