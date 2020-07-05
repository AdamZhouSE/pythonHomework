#有更好解法，用数组删除
n,m=map(int,input().split())
l=list(map(int,input().split()))
sign=n
while sign>1:
    for i in range(0,len(l)):
        if l[i]<=m and l[i]!=-1:
            l[i]=-1
            sign-=1
        if l[i]>m:
            l[i]-=m
        if sign==1:
            break
child=0
for j in range(0,len(l)):
    if l[j]!=-1:
        child=j+1
        break
print(child)