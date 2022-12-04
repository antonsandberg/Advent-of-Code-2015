from itertools import count
from hashlib import md5

data = "iwrupvqb"

for x in count(1):
    test = data + str(x)
    if md5(test.encode()).hexdigest()[:6] == '000000':
        print(x)
        break
