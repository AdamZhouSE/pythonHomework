n = int(input())
nums = input().split()
for i in range(0, len(nums)):
    nums[i] = int(nums[i])


gotIt = True
for i in nums:
    gotIt = True
    for j in nums:
        if j / i != j // i:
            gotIt = False
    if gotIt:
        print(i)
        break
if not gotIt:
    print(-1)