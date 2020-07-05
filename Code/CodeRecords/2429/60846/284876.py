t=int(input())
for i in range(t):
    n=int(input())
    ret=0
    nums=[int(x) for x in input().split()]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j]-nums[i]>ret:
                ret=nums[j]-nums[i]
    print(ret)