nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
v = int(input())
index = -1
for i in range(0, len(num)):
    if num[i] == v:
        index = i
print(index)