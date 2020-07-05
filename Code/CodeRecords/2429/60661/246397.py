t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ');nums=[int(x) for x in nums]
    start=0;res=0
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            start=i
        else:
            res=max(res,nums[i]-nums[start])
    print(res)