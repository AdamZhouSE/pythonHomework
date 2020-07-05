def main():
    times = eval(input())
    nums = []
    for i in range(0, len(times)):
        x, y = map(int, times[i].split(":"))
        nums.append(60 * x + y)
    nums = sorted(nums)
    gaps = []
    for i in range(0, len(nums)):
        if i != len(nums) - 1:
            gaps.append(nums[i + 1] - nums[i])
        else:
            gaps.append(1440 - nums[i] + nums[0])
    print(min(gaps))


if __name__ == '__main__':
    main()
