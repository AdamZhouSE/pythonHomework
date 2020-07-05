def cal(last,n):
    sum=0
    if n==1:
        return last//2
    if last==0:
        return 0

    i=last//2
    while i>=2**(n-1):
        sum+=cal(i,n-1)
        i-=1
    return sum

n=int(input())
for i in range(n):
    temp=input().split(" ")
    m=int(temp[0])
    n=int(temp[1])
    sum=0
    i=m
    while i>=2**(n-1):
        sum+=cal(i,n-1)
        i-=1

    print(sum)