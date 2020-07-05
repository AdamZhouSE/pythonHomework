n=int(input())
def func(c,k,m):
    if(k==0):
        return 1
    else:
        temp=[]
        x=c*2
        while(x*pow(2,k-1)<=m):
            temp.append(x)
            x=x+1
        re=[]
        for i in temp:
            re.append(func(i,k-1,m))
        return sum(re)
for i in range(n):
    s=input()
    sl=s.split( )
    m=int(sl[0])
    k=int(sl[1])
    fir=[]
    x=1
    while x*pow(2,k-1)<=m:
        fir.append(x)
        x=x+1
    re=[]
    for c in fir:
        re.append(func(c,k-1,m))
    print(sum(re))
