def ans(nums):
    if(len(nums)==1):
        if(nums[0]==0):
            return "UP"
        elif(nums[0]==15):
            return "DOWN"
        else:
            return -1
    if(nums[-1]==15):
        return "DOWN"
    if(nums[-1]==0):
        return "UP"
    if(nums[-1]>nums[-2]):
        return "UP"
    else:
        return "DOWN"

n = int(input())
temp = input().split(" ")
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))
