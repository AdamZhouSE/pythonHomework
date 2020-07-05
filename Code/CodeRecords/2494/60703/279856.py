nums  = eval(input())
n = len(nums)
res = 0
for i in range(n):
    for j in range(i+1,n):
        if(nums[i]>nums[j]*2):
            res+=1
print(res)