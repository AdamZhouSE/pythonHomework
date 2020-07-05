


def solve():
    line = sorted(list(input()))
    num = []
    while 'z' in line:
        num.append(0)
        del line[line.index('z')]
        del line[line.index('e')]
        del line[line.index('r')]
        del line[line.index('o')]
    while 'w' in line:
        num.append(2)
        del line[line.index('t')]
        del line[line.index('w')]
        del line[line.index('o')]
    while 'u' in line:
        num.append(4)
        del line[line.index('f')]
        del line[line.index('o')]
        del line[line.index('u')]
        del line[line.index('r')]
    while 'x' in line:
        num.append(6)
        del line[line.index('s')]
        del line[line.index('i')]
        del line[line.index('x')]
    while 'g' in line:
        num.append(8)
        del line[line.index('e')]
        del line[line.index('i')]
        del line[line.index('g')]
        del line[line.index('h')]
        del line[line.index('t')]
    while 'o' in line:
        num.append(1)
        del line[line.index('o')]
    while 'r' in line:
        num.append(3)
        del line[line.index('r')]
    while 's' in line:
        num.append(7)
        del line[line.index('s')]
    while 'f' in line:
        num.append(5)
        del line[line.index('i')]
        del line[line.index('f')]
    while 'i' in line:
        num.append(9)
        del line[line.index('i')]

    num.sort()
    for i in range(0,len(num)):
        print(num[i],end = '')
    print()

solve()
