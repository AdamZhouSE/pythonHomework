import math

t = int(input())
i = t
res = list()
while i > 0:
    n, k = map(int, input().split())
    i = i - 1
    res.append(pow(k, n - 1))

while i<n:
    print(res[i])
    i=i+1