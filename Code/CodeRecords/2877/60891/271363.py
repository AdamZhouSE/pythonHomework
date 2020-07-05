n = int(input())
a = [int(i) for i in input().split()]
res = 0
for i in range(n):
    res += abs(a[i])
print(res)
