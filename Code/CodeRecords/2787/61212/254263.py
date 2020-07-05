num = int(input())
lists = list(input().split(" "))
nums = []

for i in range(0, num):
    nums.append(int(lists[i]))

nums.sort()

res = 0
for i in range(0, num):
    if i + 1 >= nums[i]:
        res = res + i + 1 - nums[i]
    else:
        res = res + nums[i] - i - 1

print(res)
