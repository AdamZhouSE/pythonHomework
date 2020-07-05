def main():
    nums = eval(input())
    nums = sorted(nums)
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i] - nums[i - 1]
    del nums[len(nums) - 1]
    print(max(nums))


if __name__ == "__main__":
    main()