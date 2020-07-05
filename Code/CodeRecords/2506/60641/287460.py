def main():
    nums = eval(input())
    for i in range(0, len(nums) - 1):
        nums[i] = nums[i + 1] - nums[i]
    nums = nums[:len(nums) - 1]
    result = []
    minus = []
    for i in range(0, len(nums)):
        if nums[i] < 0:
            minus.append(i)
    minus.insert(0, 0)
    minus.append(len(nums))
    for i in range(0, len(minus) - 1):
        result.append(nums[minus[i]:minus[i + 1]])
    result = sorted(result, key=lambda x: len(x), reverse=True)
    print(len(result[0]))


if __name__ == '__main__':
    main()
