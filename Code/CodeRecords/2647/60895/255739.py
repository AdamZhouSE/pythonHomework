t=int(input())
while t>0:
    t=t-1
    n=int(input())
    num=0
    while n>0:
        index=1
        while n>=index:
            index=index*2
        index=index/2
        n=n-index
        num=num+1
    print(num)