t=int(input())
for tt in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    single=0
    double=0
    ans=0
    for i in arr:
        if(i%3==0):
            ans+=1
        elif(i%3==1):
            single+=1
        else:
            double+=1
    if(single<double):
        ans+=single+int((double-single)/3)
    else:
        ans+=double+int((single-double)/3)
    print(ans)
