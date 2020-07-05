nums=int(input())
for i in range(nums):
    [a,b,m]=list(map(int,input().split(" ")))
    start=a//m
    temp=m*start
    count=0
    while temp<=b:
        if temp>=a:
           count+=1
        temp+=m
    print(count)