num = int(input())
nums = input().split()
for i in range(0, num):
    nums[i] = int(nums[i])
sum = 0
for i in nums:
    if i < 0:
        sum += -i
    else:
        sum += i
print(sum)