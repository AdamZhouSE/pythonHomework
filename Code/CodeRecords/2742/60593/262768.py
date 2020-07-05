import heapq
def lower_bound(target):
    low, high = 0, len(tmp)-1
    pos = len(tmp)
    while low<high:
        mid = (low+high)//2
        if tmp[mid] < target:
            low = mid+1
        else:
            high = mid
    if tmp[low]>=target:
        pos = low
    return pos
n=int(input())
a=[[]]
for t in range(n):
    v,opt,x=map(int,input().split())
    tmp=a[v].copy()
    if(opt==1):
        tmp.append(x)
        a.append(tmp)
    elif(opt==2):
        for i in range(len(tmp)):
            if(tmp[i]==x):
                del tmp[i]
                break
        a.append(tmp)
    elif(opt==3):
        sav=tmp.copy()
        a.append(sav)
        tmp.sort()
        print(lower_bound(x)+1)
    elif(opt==4):
        sav=tmp.copy()
        a.append(sav)
        print(list(heapq.nsmallest(x,tmp))[x-1])
    else:
        sav=tmp.copy()
        a.append(sav)
        tmp.sort()
        if(opt==5):
            ans=-2**31+1
            for i in range(len(tmp)-1,-1,-1):
                if(tmp[i]<x):
                    ans=tmp[i]
                    break
            print(ans)
        else:
            ans=2**31
            for i in range(len(tmp)):
                if(tmp[i]>x):
                    ans=tmp[i]
                    break
            print(ans)


