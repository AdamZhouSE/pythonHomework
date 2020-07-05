T=int(input())
for a in range(0,T):
    n=int(input())
    tem=n
    count=0
    while(n>=2):
        n=n//2
        count=count+1
    t=1
    while(t<=count+1):
        res=0
        if(t%2==1):
            for x in range(0,t,2):
                res=res+pow(2,x)
        else:
            for y in range(1,t,2):
                res=res+pow(2,y)
        t=t+1
        if(res<=tem):
            print(res,end="")
        if(t!=count+2 and res!=85):
            print(" ",end="")
    print()