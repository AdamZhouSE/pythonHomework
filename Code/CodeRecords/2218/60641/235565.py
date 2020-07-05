def main():
    nums = list(map(int, input().split(",")))
    nums.sort()
    l = len(nums)
    print(nums[l - 1] * max(nums[0] * nums[1], nums[l - 2] * nums[l - 3]))


if __name__ == '__main__':
    main()