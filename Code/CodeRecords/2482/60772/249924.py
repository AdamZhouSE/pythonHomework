import sys


def execute(n, d):
    print(int(n / d), end='')
    k = n % d
    if k == 0:
        print()
        return
    i = 0
    frac = [k]
    start = -1
    while True:
        k = (k * 10) % d
        if k == 0:
            break
        if k in frac:
            start = frac.index(k)
            break
        frac.append(k)
        i += 1

    print('.', end='')
    for i in range(len(frac)):
        if i == start: print('(', end='')
        print(int((frac[i] * 10) / d), end='')
    if start > -1:
        print(')')
    else:
        print()


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])
    D = int(Input[begin + 1])
    begin += 2
    execute(N, D)
