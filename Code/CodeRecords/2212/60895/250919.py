t=int(input())
while t>0:
    x=int(input())
    t=t-1
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum=sum+i
    if sum<x:
        print(1)
    else:
        print(0)