if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    n = len(nums)
    average = 0
    if (sum(nums) % n)/float(n) <= 0.5:
        average = int(sum(nums) / n)
    else:
        average = int(sum(nums)/n) + 1
    res = 0
    for num in nums:
        res += abs(num - average)