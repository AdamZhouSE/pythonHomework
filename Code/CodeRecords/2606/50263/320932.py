nums = eval(input())
target = int(input())
if target not in nums:
    print(-1)
else:
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)