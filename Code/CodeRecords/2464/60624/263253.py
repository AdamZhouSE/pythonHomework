def func8():
    target = int(input())
    nums = list(map(int, input().split(",")))
    low, high, res = 0, len(nums), 0
    def helper(size):
        sum_size = 0
        for i in range(len(nums)):
            sum_size += nums[i]
            if i >= size:
                sum_size -= nums[i-size]
            if sum_size >= target:
                return True
        return False
    while low <= high:
        mid = (low+high)//2
        if helper(mid):
            res = mid
            high = mid-1
        else:
            low = mid+1
    print(res)
    return
func8()