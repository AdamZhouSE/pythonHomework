from collections import defaultdict


ns = int(input())
adds = defaultdict(list)
cnt = 1
for n in range(ns):
    formula = input().split()
    if formula[0] == 'Add':
        adds[cnt] = list(map(int, formula[1:]))
        cnt += 1
    elif formula[0] == 'Del':
        adds.pop(int(formula[1]))
    else:
        k = int(formula[1])
        ans = 0
        for f in adds.values():
            if f[0] * k + f[1] > f[2]:
                ans += 1
        print(ans)
