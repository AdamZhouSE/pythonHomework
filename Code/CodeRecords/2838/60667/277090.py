import math
n = int(input())
a = list(map(int, input().split()))
temp = []
a.sort()
for i in range(n):
    temp.append(pow(a[i]+a[n-1-i], 2))
print(int(sum(temp)/2))