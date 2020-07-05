t=int(input())
for tt in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    pt=-1
    times={}
    for i in a:
        if(i not in times):
            times[i]=1
        else:
            times[i]+=1
    for i in a:
        if(times[i]==1):
            if(k==1):
                pt=i
                break
            else:
                k-=1
    print(pt)
            