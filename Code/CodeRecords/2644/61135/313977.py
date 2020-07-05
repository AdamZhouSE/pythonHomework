A=eval(input())
K=int(input())
if(sum(A)<K):
    print(-1)
else:
    minl=1
    for a in range(1,len(A)+1):
        lef=0
        rig=a
        while(rig-1<len(A)):
            mid=0
            for b in range(lef,rig):
                mid=mid+A[b]
            if(mid==K):
                minl=a
                break
            lef=lef+1
            rig=rig+1
    print(minl)