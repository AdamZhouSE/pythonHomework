n=int(input()[1:-1])
Max=int(math.log(n,2))
while True:
    low=max(int(math.pow(n/2,1/(Max-1))),2)
    high=int(math.pow(n, 1.0 / (Max - 1)))+1
    tmp=n
    while low<high:
        mid=(low+high)//2
        tmp=0
        for i in range(Max):
            tmp=tmp*mid+1
        if tmp<n:
            low=mid+1
        elif tmp>n:
            high=mid
        else:
            low=high=mid
    if tmp==n:
        print(low)
        break
    elif Max==1:
        print(0)
        break
    else:
        Max-=1