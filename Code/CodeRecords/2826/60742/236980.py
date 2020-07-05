n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
num = 0
for i in range(1,n):
    while a[i]<=a[i-1]:
        a[i] += 1
        num += 1
print (num)