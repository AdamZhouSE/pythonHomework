import re
title = input()
pattern = re.compile('[0-9]+')
a = pattern.findall(title)
a = [int(x) for x in a]
k = int(input())
x = int(input())
res = list()
for i in range(len(a)):
    res.append([abs(x-a[i]), a[i]])


res.sort()
ans = list()
for i in range(k):
    ans.append(res[i][1])
ans.sort()
print(ans)
