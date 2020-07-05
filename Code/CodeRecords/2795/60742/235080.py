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
if len(l)>3:
    res = -1
elif len(l)==3:
    if l[0]+l[2]==2*l[1]:
        res = l[1]-l[0]
    else:
        res = -1
elif len(l)==2:
    if (l[0]+l[1])%2==0:
        res = (l[1]-l[0])//2
    else:
        res = l[1]-l[0]
else:
    res = 0
print (res)