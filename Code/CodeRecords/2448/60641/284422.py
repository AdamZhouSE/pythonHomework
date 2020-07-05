def main():
    nums = sorted(eval(input()), reverse=True)
    result = 0
    if min(nums) >= len(nums):
        result = len(nums)
    elif max(nums) == 0:
        result = 0
    else:
        for i in range(0, len(nums) - 1):
            if nums[i] >= i + 1 and nums[i + 1] < i + 2:
                result = i + 1
                break
    print(result)


if __name__ == '__main__':
    main()
