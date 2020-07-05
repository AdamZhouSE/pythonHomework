def method(k, nums):
    n = len(nums)
    ans = n
    left = 0
    sum = 0
    for i in range(n):
        sum += nums[i]
        while sum >= k:
            ans = min(ans, i + 1 - left)
            sum -= nums[left]
            left += 1
    return ans


if __name__ == '__main__':
    print(method(eval(input()), eval(input())))