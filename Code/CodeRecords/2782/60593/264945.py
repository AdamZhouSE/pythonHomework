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
    return min(p,t)
a=[(0,0)]
n=int(input())
for i in range(1,n+1):
    x=int(input())
    a.append((i,x))
a.sort(key=lambda y:y[1])
summ=0
for i in range(1,n+1):
    summ+=chk(i)
print(summ)