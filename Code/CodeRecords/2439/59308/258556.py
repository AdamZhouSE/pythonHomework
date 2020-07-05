import re
import collections
n = int(input())
pattern = re.compile('[0-9]+')
res = collections.defaultdict(dict)
temp = list()
for i in range(n-1):
    a = [int(x) for x in pattern.findall(input())]
    u, v, w = a[0], a[1], a[2]
    temp.append(a)
    res[u][v] = w

# print(res[2])
m = int(input())
for i in range(m):
    a = pattern.findall(input())
    u, v = int(a[0]), int(a[1])
    temp.append(a)
    if u == v:
        print(0)
        continue
    start = u
    end = list(res[u].keys())[0]
    ans = res[u][end]
    while end != v:
        try:
            start = end
            end = list(res[start].keys())[0]
            ans = ans ^ res[start][end]
        except IndexError:
            ans = 101
            break
    print(ans)


