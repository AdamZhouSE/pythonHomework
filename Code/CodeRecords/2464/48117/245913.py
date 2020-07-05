s = int(input())
nums = input().split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

count = 0

if sum(nums) < s:
    print(0)
else:
    nums.sort()
    for i in range(len(nums) - 1, -1 , -1):
        if s > 0:
            s -= nums[i]
            count += 1
        else:
            break
    print(count)