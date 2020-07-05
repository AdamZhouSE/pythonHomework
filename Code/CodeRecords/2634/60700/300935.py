import re
line = input()
k = int(input())
a = re.split(r"[\[\], ]+", line)
for i in range(a.count('')):
    a.remove('')
for i in range(len(a)):
    a[i] = int(a[i])
"""暴力解法先顶上orz"""
f = []
ans = []
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        f.append([a[i] / a[j], [a[i], a[j]]])
f.sort(key=lambda x:x[0])
print(f[k - 1][1])
