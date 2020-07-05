t=int(input())
for _ in range(t):
    n=int(input())
    nums = input().split(' ')
    nums = [int(x) for x in nums]
    res=0
    for i in range(n):
        temp=res
        for j in range(temp,i+1):
            if nums[i-j]<nums[i]:
                res=j
    print(res)
    if(res==4):
        print(nums)