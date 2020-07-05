def f(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return s[0]
    elif len(s[0]) == 1:
        t = []
        for ele in s:
            t += s
        return t
    else:
        t = []
        t += s.pop(0)
        for rest in s:
            t .append( rest.pop())
        m = s.pop()
        m.reverse()
        t += m
        for i in range(len(s) - 1, -1, -1):
            t.append( s[i].pop(0))
        return t + f(s)


a = int(input().strip())
for i in range(a):
    line = input().strip()
    length1 = int(line.split()[0])
    length2 = int(line.split()[1])
    x = []
    y = [int(l) for l in input().strip().split()]
    for p in range(length1):
        x.append(y[p * length2:p * length2 + length2])

    print(' '.join([str(l) for l in f(x)]),end=' ')
    print()

