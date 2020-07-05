t=int(input())
while t>0:
    t=t-1
    n=int(input())
    i=2*n-1
    temp=1
    num=0
    while temp<=n:
        num=num+i*temp
        i=i-2
        temp=temp+1
    print(num)