def main():
    nums = list(map(int, input().split(",")))
    key = int(input())
    lower = -1
    upper = -1
    try:
        lower = nums.index(key)
        upper = len(nums) - 1 - sorted(nums, reverse=True).index(key)
    except ValueError:
        pass
    print([lower, upper])


if __name__ == "__main__":
    main()
