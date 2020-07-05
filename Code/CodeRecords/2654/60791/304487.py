
a = [0]*1000
n = int(input())
num = set()
res = 0
for i in range(n):
    ai,bi,hi = [int(i) for i in input().split(' ')]
    for j in range(ai,bi):
        a[j] = max(a[j],hi)
        num.add(j)
for item in num:
    res += a[item]
print(res)