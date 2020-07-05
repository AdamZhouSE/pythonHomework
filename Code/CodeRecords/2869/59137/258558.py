def s13():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])
    nums = list(reversed(nums))

    index = 0
    while True:
        x = nums[index]
        while nums.count(x) > 1:
            t = nums[index+1:].index(x)
            nums.pop(t + index + 1)
        if len(nums) == index+1:
            break
        index = index + 1
    nums = list(reversed(nums))
    print(len(nums))
    for x in range(len(nums)-1):
        print(nums[x], "", end="")
    print(nums[len(nums)-1])


s13()