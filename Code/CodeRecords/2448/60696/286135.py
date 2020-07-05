def h_exponent(nums:list)->int:
    res = 0
    n = len(nums)
    nums.sort(reverse=True)
    while res < n:
        if nums[res] < res:
            break
        res += 1
    return res


if __name__ == '__main__':
    nums = eval(input())
    print(h_exponent(nums))
