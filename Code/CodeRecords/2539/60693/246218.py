nums=eval(input())
nums_sorted=sorted(nums)
start,end=0,0
for i in range(len(nums)):
    if nums[i]!=nums_sorted[i]:
        start=i
        break
for j in range(len(nums)-1,0,-1):
    if nums[j]!=nums_sorted[j]:
        end=j
        break
print(end-start+1)