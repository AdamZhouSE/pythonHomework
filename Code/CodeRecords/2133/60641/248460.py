def main():
    nums = list(map(int, input().split(",")))
    count = 0

    while min(nums) is not max(nums):
        index_of_max = nums.index(max(nums))

        for i in range(0, len(nums)):
            if i is index_of_max:
                continue
            else:
                nums[i] += 1

        count += 1

    print(count)


if __name__ == "__main__":
    main()
