nums=int(input())
for i in range(nums):
    [m,n]=list(map(int,input().split(" ")))
    if m>=n*(n+1)/2:
        print(1)
    else:
        print(0)