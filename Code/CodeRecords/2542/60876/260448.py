nums=eval(input())
nums.sort()
max=1
length=len(nums)
for start in range(0,length):
    ind=start+1
    while ind!=length and nums[ind]-nums[ind-1]==1:
        ind+=1
    if ind-start>max:
        max=ind-start
print(max)