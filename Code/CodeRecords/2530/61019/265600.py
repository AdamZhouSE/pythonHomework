s1 = input()
s2 = input()
tbl = {}
for k, v in enumerate(s1):
    tbl[v] = k
s2 = [(k, tbl[k] if k in tbl else -1) for k in s2]
s2.sort(key=lambda a: a[1])
print(''.join([k for k, v in s2]))
