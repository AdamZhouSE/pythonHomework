nums=list(eval(input()))
res=1
before=[nums[0]]
for i in range(1,len(nums)):
    if max(before)<min(nums[i:]):
        res+=1
        before=[nums[i]]
    else:
        before.append(nums[i])
print(res)