def func15():
    nums = list(map(int, input().split(",")))
    m = int(input())
    if len(nums) == m:
        return max(nums)
    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low+high) // 2
        temp, cnt = 0, 1
        for num in nums:
            temp += num
            if temp > mid:
                temp = num
                cnt += 1
        if cnt > m:
            low = mid+1
        else:
            high = mid
    return low
print(func15())