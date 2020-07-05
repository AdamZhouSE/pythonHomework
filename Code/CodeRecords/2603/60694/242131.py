def smallestDistancePair(nums: [int], k: int) -> int:
    n = len(nums)
    nums.sort()

    def count(K: int) -> int:
        cnt, l = 0, 0
        for r in range(n):
            while l < r and nums[r] - nums[l] > K:
                l += 1
            cnt += r - l
        return cnt

    l, r = 0, nums[-1] - nums[0]
    while l < r:
        m = (l + r) // 2
        if count(m) >= k:
            r = m
        else:
            l = m + 1
    return l


a = eval(input())
print(smallestDistancePair(a, int(input())))
