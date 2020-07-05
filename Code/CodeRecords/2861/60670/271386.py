n=int(input())
a=sorted(list(map(int,input().split())))
sumn=0
for i in range(0,n//2):
    sumn=sumn+a[2*i+1]-a[2*i]
print(sumn)