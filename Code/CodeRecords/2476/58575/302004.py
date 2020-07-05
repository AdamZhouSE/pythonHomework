res=[]
n=int(input())
for i in range(n):
    number=int(input())
    nums=list(map(int,input().split(" ")))
    nums.sort()
    
    while len(nums)!=1:
        nums[1]=nums[1]+nums[0]
        res.append(nums[1])
        nums=nums[1:]
        nums.sort()
    sum=0
    for k in res:
        sum+=k
    print(sum)
    res.clear()