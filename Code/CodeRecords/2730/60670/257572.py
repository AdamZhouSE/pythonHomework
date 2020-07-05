def getsum(x):
    sum=0
    while x>0:
        sum=sum+x%10
        x=x//10
    return sum

t=int(input())
for k in range(0,t):
    n=int(input())
    nums=list(map(int,input().split()))
    sum=0
    for num in nums:
        sum+=getsum(num)
    if sum%3==0:
        print(1)
    else:
        print(0)