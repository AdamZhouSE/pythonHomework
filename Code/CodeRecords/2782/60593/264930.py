def chk(x):
    p,t=2**31-1,2**31-1
    if(a[x][0]==1):
        return a[x][1]
    for i in range(x-1,0,-1):
        if(a[i][0]<a[x][0]):
            p=abs(a[i][1]-a[x][1])
            break
    for i in range(x+1,n+1):
        if(a[i][0]<a[x][0]):
            t=abs(a[i][1]-a[x][1])
    return max(p,t)
a=[]
n=int(input())
for i in range(1,n+1):
    x=int(input())
    a.append(i,x)
a.sort()
summ=0
for i in range(1,n+1):
    summ+=chk(i)
print(summ)