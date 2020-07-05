def longest_continuous_sl(nums):
    ans = 1
    tmp = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1
    return ans


if __name__ == '__main__':
    print(longest_continuous_sl(eval(input())))