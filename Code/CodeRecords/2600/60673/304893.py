def maxSum(nums):
    sum=0
    res=[]
    for i in range(len(nums)):
        if(nums[i]!=-1):
            sum+=nums[i]
        else:
            res.append(sum)
            sum=0
    res.append(sum)
    return max(res)
            
def destruct(nums,ind):
    nums[ind]=-1
    print(maxSum(nums))

n=int(input())
nums=input().split(" ")
order=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
    order[i]=int(order[i])
for i in range(n):
    destruct(nums,order[i]-1)

