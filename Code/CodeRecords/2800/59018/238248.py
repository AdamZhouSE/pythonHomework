n,d=input().split(' ')
info=input().split(' ')
a=[int(y) for y in info]
count=0
c=[]
for i in range(int(n)-1):
    while(a[i+1]<=a[i]):
        a[i+1]=a[i+1]+int(d)
        c.append(1)
print(sum(c))