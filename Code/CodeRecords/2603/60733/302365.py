def smallestDistancePair(nums, k) -> int:
    nums.sort()
    left, right = 0, nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2
        cnt, start = 0, 0
        for i in range(len(nums)):
            while nums[i] - nums[start] > mid:
                start += 1
            cnt += i - start
        if cnt < k:
            left = mid + 1
        else:
            right = mid
    return left


s = input().replace("[", "").replace("]", "")
k = list(map(int, s.split(",")))
n = int(input())
res = smallestDistancePair(k, n)
print(res)
