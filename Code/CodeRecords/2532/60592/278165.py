nums = eval(input())
res = 0
i= 0
while i < len(nums):
    if i < len(nums)-1 and nums[i+1]<=nums[i]:
        i+=1
        continue
    tem = nums[0:i+1]
    if i < len(nums)-1 and nums[i+1]>=tem[len(tem)-1]:
        i+=1
        continue
    res+=1
    i+=1
print(res)