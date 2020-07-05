nums=eval(input())
nor=sorted(nums)
result=len(nums)
length=len(nums)
for i in range(0,length):
    if nums[i]!=nor[i]:
        result-=i
        break
for i in range(0,length):
    if nums[length-1-i]!=nor[length-1-i]:
        result-=i
        break
print(result)