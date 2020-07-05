def find_max_index(temp):
    index = 0
    m = 0
    for i in range(len(temp)):
        if temp[i] > m:
            m = temp[i]
            index = i
    return index

import re
title = input()
pattern = re.compile('[0-9]+')
a = pattern.findall(title)
n, m = int(a[0]), int(a[1])
res = [0 for _ in range(n)]
for i in range(m):
    a = pattern.findall(input())
    a = [int(x) for x in a]
    res[find_max_index(a)] += 1

print(find_max_index(res)+1)





