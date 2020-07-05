def find(nums):
    target = 0
    for i in range(1, len(nums)):
        target += i
    for num in nums:
        target -= num
    print(-target)

nums = list(map(int, input().split(',')))
find(nums)