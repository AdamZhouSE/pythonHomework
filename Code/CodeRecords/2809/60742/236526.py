n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
la = lb = 0
num = n//2
for i in range(num):
    min_len = min(a)
    la += min_len
    a.remove(min_len)
for j in a:
    lb += j
res = la**2 + lb**2
print (res)