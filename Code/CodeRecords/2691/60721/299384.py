T=int(input())
for o in range(0,T):
    n=int(input())
    lis=list(map(int ,input().split(" ")))
    lis.sort()
    a=0
    b=0
    count=0
    p=int(len(lis)/2)
    if(len(lis)==2):
        print(lis[1]-lis[0])
        continue
    else:
        while(count!=p):
            a+=lis[0]
            a+=lis[len(lis)-1]
            lis.pop(0)
            lis.pop(len(lis)-1)
            count+=2
        for i in lis:
            b+=i
        
        if(int(max(a,b)-min(a,b))==2):
            print(0)
            continue
        print(int(max(a,b)-min(a,b)))