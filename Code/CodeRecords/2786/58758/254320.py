days = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
count = 0
for i in range(0, days):
    flag = False
    for j in range(0, len(nums)):
        if nums[j] >= i+1:
            flag = True
            nums.pop(j)
            count += 1
            break
    if not flag:
        break
print(count)
