t=int(input())
while t>0:
    n=int(input())
    temp=n
    start=0
    sum=0
    if n==1:
        sum=3
    else:
        temp=temp-1
        while temp>0:
            start=start+2*temp
            temp=temp-1
        for i in range(0,2*n):
            sum=sum+start+i+1
    print(sum)