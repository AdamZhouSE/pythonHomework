nums = eval(input())
nums.sort()
res = 1
n = len(nums)
for i in range(n-1):
    if(nums[i+1]-nums[i]==1):
        res+=1
print(res)    