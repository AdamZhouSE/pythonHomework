t = int(input())
for k in range(t):
    s1 = set(input())
    s2 = set(input())
    s_diff = (s1.difference(s2)).union(s2.difference(s1))
    res = []
    while s_diff:
        res.append(s_diff.pop())
    res.sort()
    print(''.join(res))
    print()
