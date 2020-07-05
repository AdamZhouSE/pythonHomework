import re

pattern = re.compile('[0-9]+')
a = [int(x) for x in pattern.findall(input())]
n, m = a[0], a[1]
res = []
for i in range(n):
    res.append([input(), i + 1])

res.sort(key=lambda x: x[0], reverse=True)
for i in range(m):
    a = [int(x) for x in pattern.findall(input())]
    left = a[0]
    right = a[1]
    for j in range(len(res)):
        if left <= res[j][1] <= right:
            break
    print(res[j][0])








