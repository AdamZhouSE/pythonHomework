# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

# [1,2,0]
# 3

nums = input()[1:-1].split(',')
for j in range(len(nums)):
    nums[j] = int(nums[j])

i = 0
while True:
    i += 1
    if i not in nums:
        print(i)
        break
