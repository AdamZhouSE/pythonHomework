number=int(input())
i=2
while True:
    sum=0
    exp=0
    while sum<number:
        sum=sum+int(pow(i,exp))
        exp=exp+1
    if sum==number:
        print(i)
        break
    else:
        i=i+1