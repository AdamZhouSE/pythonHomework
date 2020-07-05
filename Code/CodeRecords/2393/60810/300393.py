def test(m,n,x,y):
    res=0
    for i in range(m):
        for j in range(n):
            if(pow(x[i],y[j])>pow(y[j],x[i])):
                res+=1
    return res

t=int(input())
for i in range(t):
    mn=input().split(" ")
    m=int(mn[0])
    n=int(mn[1])
    x=input().split(" ")
    y=input().split(" ")
    for i in range(m):
        x[i]=int(x[i])
    for i in range(n):
        y[i]=int(y[i])
    print(test(m,n,x,y))