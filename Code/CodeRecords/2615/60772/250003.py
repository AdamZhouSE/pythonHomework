import sys
from collections import Counter


def execute(s):
    s = list(map(ord, s))
    s = list(set(s))
    s.sort(reverse=True)
    li = Counter(s)
    st, max, diff = 0, 0, 0
    for j in range(1, 13, 1):
        for k in range(len(s)):
            length = 1
            a = s[k]
            while (li[a - j] > 0):
                a -= j
                length += 1
            if length > max:
                diff = j
                max = length
                st = s[k]
    for x in range(max, 0, -1):
        print(chr(st), end='')
        st -= diff
    print()


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    #info = Input[begin].split()
    #N = int(info[0])
    s = Input[begin]

    begin += 1

    execute(s)

