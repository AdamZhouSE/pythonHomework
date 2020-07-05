n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
b=[]
c=[]
for i in range(n):
    while(a[i]%2==0):
        a[i]=a[i]//2
    b.append(a[i])
for j in range(len(b)):
    while(b[j]%3==0):
        b[j]=b[j]//3
    c.append(b[j])

d=set(c)
if len(list(d))==1:
    print("Yes")
else:
    print("No")
    