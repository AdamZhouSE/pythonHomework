def ans(nums):
    temp = sorted(nums)
    for i in range(0,len(nums)):
        if(nums[i]!=temp[i]):
            start = i
            break
    for i in range(len(nums)-1,-1,-1):
        if (nums[i] != temp[i]):
            end = i
            break
    return end-start+1

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))