nums = eval(input())
res = 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]>2*nums[j]:
            res += 1
print(res)