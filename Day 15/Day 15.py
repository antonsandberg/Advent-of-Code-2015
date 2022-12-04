import numpy as np


with open('input.txt') as f:
    s = [x.strip().split() for x in f.readlines()]


best_final_result = 0
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            d = 100-a-b-c
            caps = []
            durs = []
            texs = []
            cals = []
            flavs = []

            x = [a, b, c, d]
            for row in s:
                _, _, cap, _, dur, _, flav, _, tex, _, cal = row
                cap, dur, tex, flav, cal = [x.strip(',') for x in [cap, dur, flav, tex, cal]]
                cap = int(cap)
                dur = int(dur)
                tex = int(tex)
                cal = int(cal)
                flav = int(flav)

                caps.append(cap)
                durs.append(dur)
                texs.append(tex)
                cals.append(cal)
                flavs.append(flav)
            variables = []
            total_cals = np.sum(np.multiply(cals, x))
            if not (total_cals == 500):
                continue
            for i in [caps, durs, texs, flavs]:

                result = np.sum(np.multiply(i, x))

                result = max(0, result)
                variables.append(result)

            final_result = 1
            for j in range(len(variables)):
                final_result = final_result*variables[j]

            best_final_result = max(best_final_result, final_result)
print(best_final_result)


