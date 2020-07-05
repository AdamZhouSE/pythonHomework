if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = [int(a) for a in input().split()]
        nums.sort()
        res = sum(nums)
        for j in range(1, n):
            s = nums[:j]
            t = nums[j:]
            sum1 = sum(s)
            sum2 = sum(t)
            res = min(res, abs(sum1 - sum2))
        print(res)