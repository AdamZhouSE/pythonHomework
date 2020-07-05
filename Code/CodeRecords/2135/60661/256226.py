nums=list(eval(input()))
average=round(sum(nums)/len(nums))
res=0
for i in range(len(nums)):
    res+=abs(nums[i]-average)
print(res)