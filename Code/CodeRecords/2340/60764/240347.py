T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    rain=0
    high=0
    if max(nums)==nums[high]:
        high=n-1
    for i in range(1,n):
        if nums[i]<nums[high]:
            rain+=nums[high]-nums[i]
        else:
            high=i
    print(rain)