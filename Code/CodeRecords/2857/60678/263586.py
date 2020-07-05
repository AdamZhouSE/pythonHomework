def goodTogo(nums, min):
    for i in nums:
        if i % min != 0:
            return False
    return True

n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])

min = nums[0]
hasSingle = False
for i in range(0, n):
    if nums[i] < min:
        min = nums[i]
    if nums[i] % 2 != 0:
        hasSingle = True

count = 0
potiantials = []
for i in range(1, min + 1):
    if hasSingle and i % 2 == 0:
        continue
    if min % i == 0:
        potiantials.append(i)

for i in potiantials:
    if goodTogo(nums, i):
        count += 1
print(count)