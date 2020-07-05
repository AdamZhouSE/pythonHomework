t=int(input())
while t>0:
    n=int(input())
    t=t-1
    times=1
    result=0
    while n>0:
        result=result+n*times
        times=times+1
        n=n-1
    print(result)