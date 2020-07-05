nums=eval(input())
count=1
res=0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1
    else:
        if count > res:
            res=count
        count=1
print(res)