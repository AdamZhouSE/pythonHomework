def main():
    nums = eval(input())
    lower = int(input())
    upper = int(input())
    result = 0

    for i in range(1, len(nums) + 1):
        for j in range(0, len(nums) + 1 - i):
            if upper >= sum(nums[j:j + i]) >= lower:
                result += 1

    print(result)


if __name__ == "__main__":
    main()
