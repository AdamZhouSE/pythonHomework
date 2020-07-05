s = input()
t = input()
S = {}
i = 0
for si in s:
    S[si] = i
    i = i + 1
T = {}
for ti in t:
    if ti not in S:
        T[ti] = 0
        continue
    T[ti] = S[ti]
print(''.join(dict(sorted(T.items(), key=lambda kv:(kv[1],kv[0]))).keys()))