n=int(input())
for x in range(0,n):
    numbers=list(map(int,input().split(" ")))
    a=numbers[0]
    b=numbers[1]
    sum=0
    for i in range(1,b+1):
        sum=sum+i
    if sum>a:
        print(0)
    else:
        print(1)