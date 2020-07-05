t=int(input())
while t>0:
    t=t-1
    x=int(input())
    times=0
    while x>0:
        index=1
        while x>=index:
            index=index*2
        index=index/2
        x=x-index
        times=times+1
    print(times)