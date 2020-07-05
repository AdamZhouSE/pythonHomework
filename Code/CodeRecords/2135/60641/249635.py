def main():
    nums = list(map(int, input().split(",")))
    average = sum(nums) / len(nums)
    standard = round(average)
    count = 0

    for i in nums:
        count += abs(i - standard)

    print(count)


if __name__ == "__main__":
    main()