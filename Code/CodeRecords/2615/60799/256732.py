T = int(input())  # 那么慢都能过？
for ttt in range(T):
    aList = sorted(list(set(([ord(i) for i in list(input().strip())]))), reverse=True)
    res = (0, 0, 0)
    set0 = set()
    for i in aList:
        set1 = set(set0)
        for j in set1:
            if len(j) == 1:
                set0.add((j[0], i))
            elif j[-1] * 2 == i + j[-2]:
                set0.remove(j)
                L = list(j)
                L.append(i)
                set0.add(tuple(L))
        set0.add((i,))
    m = 2
    for i in set0:
        m = max(m, len(i))
    L = [i for i in set0 if len(i) == m]
    L.sort(key=lambda x: (x[0] - x[1], -x[0]))
    print(''.join(chr(i) for i in L[0]))