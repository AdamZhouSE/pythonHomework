def dele(a, N):
    if N == 0:
        return a
    else:
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1]:
                a.pop(i)
                break
        return dele(a, N - 1)

K, M = map(int, input().split())
m = []
l = [1]
while len(m) < K:
    min_l = min(l)
    m.append(min_l)
    l.append(2 * min_l + 1)
    l.append(4 * min_l + 5)
    l.remove(min_l)
s = ("".join(str(i) for i in m))
print(s)
L=list(map(int,s))
del_s = dele(L,M)
print(''.join(str(i) for i in del_s),end='')