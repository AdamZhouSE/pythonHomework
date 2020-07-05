t = int(input())
for k in range(t):
    n = int(input())
    nums = list(map(int, input().split(' ')))
    ans = 0
    if nums == sorted(nums):
        print(0)
    else:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    ans += 1
        print(ans)
