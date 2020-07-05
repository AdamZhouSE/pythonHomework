import re
pattern = re.compile('[0-9]+')
n = int(input())
a = [int(x) for x in pattern.findall(input())]
a.sort()
index = 1
res = 1
for i in range(n):
    if a[i] >= res:
        res += 1
print(res-1)





