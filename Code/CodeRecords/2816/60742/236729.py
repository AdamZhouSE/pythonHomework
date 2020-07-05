n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
for i in range(n-1):
    if i%2==0:
        a.pop()
    else:
        a.pop(0)
print (a[0])