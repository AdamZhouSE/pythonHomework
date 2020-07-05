t = int(input())
result = []
for i in range(t):
    n = int(input())
    inp = list(map(int, input().split(' ')))
    std = list(range(1, n+1))
    lost = []
    over = []
    for j in std:
        if j not in inp:
            lost.append(j)
        elif inp.count(j) > 1:
            over.append(j)
        else:
            pass
    if len(lost) == 0:
        lost.append(0)
    if len(over) == 0:
        over.append(0)
    result.append([min(over), min(lost)])
    lost.clear()
    over.clear()
for i in result:
    print(*i)
