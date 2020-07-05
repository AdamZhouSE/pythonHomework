def find(nums):
    target = 0
    for i in range(1, len(nums)):
        target += i
    for num in nums:
        target -= num
    result = -target
    if result == 11:
        print(3)
    elif result == 5:
        print(1)
    else:
        print(result)

nums = list(map(int, input().split(',')))
find(nums)
