n = int(input())
nums = ""
cnt = 1
while n > len(nums):
    nums = nums + str(cnt)
    cnt = cnt + 1
print(nums[n-1])