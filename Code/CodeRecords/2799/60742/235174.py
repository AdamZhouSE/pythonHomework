# Tip:除尽2，3后相等
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
l = []
l.append(a[0])
for i in range(1,n):
    if a[i]>a[i-1]:
        l.append(a[i])
for i in range(len(l)):
    while l[i]%2==0:
        l[i] /= 2
    while l[i]%3==0:
        l[i] /= 3
s = set(l)
if len(s)>1:
    print ("No")
else:
    print ("Yes")