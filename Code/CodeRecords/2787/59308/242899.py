import re

n = int(input())
pattern = re.compile('-*[0-9]+')
a = [int(x) for x in pattern.findall(input())]
res = 0
a.sort()
for i in range(n):
    res += abs(a[i]-(i+1))
print(res)


