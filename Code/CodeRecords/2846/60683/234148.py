n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort(reverse=True)
step = 0
openOut = False
i = 0
while not openOut:
    while i < n and nums[i] == 0:
        i += 1
    if i == n:
        openOut = True
        break
    step += 1
    j = i
    gap = nums[i]
    while j < n:
        if nums[j] != 0:
            nums[j] -= gap
        j += 1
print(step)