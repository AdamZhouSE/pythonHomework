nums=
nums.sort()
result=max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
print(result)