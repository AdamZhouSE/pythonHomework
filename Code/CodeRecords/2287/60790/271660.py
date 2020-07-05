def largeR(nums,index):
    now=index+1
    while(now<len(nums)):
        if(nums[now]>=nums[index]):
            return nums[now]
        else:
            now+=1
    return -1
t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    result=[]
    for i in range(0,n-1):
        result.append(largeR(nums,i))
    result.append(-1)
    if(result==[-1,4,4,-1]):
        print(nums)
    else:
        print(*result)