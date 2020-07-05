def ifAtoB(a,b,n):
    c=[]
    for i in range(n):
        if(a[i]>b[i]):
            return "NO"
        else:
            c.append(b[i]-a[i])
    if(len(set(c))>2):
        return "NO"
    if(len(set(c))<=1):
        return "YES"
    while (c[len(c)-1]==0):
        c=c[:-1]
    if(c!=sorted(c)):
        return "NO"
    return "YES"


t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    print(ifAtoB(a,b,n))
    
    