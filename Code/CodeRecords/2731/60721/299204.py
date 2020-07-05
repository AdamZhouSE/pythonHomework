T=int(input())
for i in range(0,T):
    n=int(input())
    s=list(map(int ,input().split(" ")))
    s.sort()
    re=0
    temp=s[0]
    count=0
    for j in s:
        count+=1
        if(temp!=j):
            temp=j
            if((count-1)%2==0):
                re+=count-1
            else:
                re+=(count-2)
            count=1
    if((count)%2==0):
        re+=count
    else:
        re+=(count-1)
    print(re)