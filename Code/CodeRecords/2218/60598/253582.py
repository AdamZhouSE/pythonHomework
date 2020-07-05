nums = sorted(list(map(int, input().split(","))))
print(max(nums[0]*nums[1]*nums[2], nums[-1]*nums[-2]*nums[-3]))
