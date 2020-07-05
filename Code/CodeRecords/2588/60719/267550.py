def f(x):
    l = []
    i = 2
    k = x**0.5
    while i <= k:
        if x % i == 0:
            l.append(i)
            x = int(x/i)
        else:
            i += 1
    if x != 1:
        l.append(x)
    return l


def g(x):
    total = 0
    x = str(x)
    l = len(x)
    for i in range(l):
        total += int(x[i])
    return total


def h(x):
    l = f(x)
    if x == l[0]:
        return 0
    total = 0
    for i in l:
        total += g(i)
    if g(x) == total:
        return 1
    else:
        return 0

s = int(input())
lst = []
for i in range(s):
    x = int(input())
    lst.append(h(x))
for i in lst:
    print(i)