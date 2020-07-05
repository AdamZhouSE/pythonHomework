n=int(input())
m=int(input())
a=[]
for i in range(0,n):
    a[i]=int(input())
a=sorted(a,reverse=True)
tmp=0
for i in range(0,n):
    tmp=tmp+a[i]
    if tmp>=m:
        print(i+1)
        break