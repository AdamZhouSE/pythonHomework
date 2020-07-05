from collections import Counter
s=input()
d = Counter(s)
res = sorted(d, key = d.get, reverse=True)
print(''.join([x*d[x] for x in res]))