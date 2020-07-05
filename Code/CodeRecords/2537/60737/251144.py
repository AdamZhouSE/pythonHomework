nums = eval(input())
k = int(input())
nums.sort(reverse=True)
print(nums[k-1])
