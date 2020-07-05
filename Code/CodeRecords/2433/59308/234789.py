import re
title = input()
pattern = re.compile('[0-9]+')
a = pattern.findall(title)
a = [int(x) for x in a]
res = list()
res.append([a[0], a[1]])
for i in range(1, len(a)-1, 2):
    if a[i] >= a[i+1]:
        res[-1][1] = a[i+2]
    else:
        res.append([a[i+1], a[i+2]])
print(res)
