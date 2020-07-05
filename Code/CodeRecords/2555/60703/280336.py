n = int(input())
nums = [int(x) for x in input().split()]
res = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(nums[i]<nums[j] and nums[j]<nums[k]):
                res+=1
print(res,end="")