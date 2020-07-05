def main():
    nums = list(map(int, input().split(",")))
    count = 0

    for i in range(3, len(nums) + 1):
        for j in range(0, len(nums) + 1 - i):
            if is_arithmetic_sequence(nums[j:j + i]):
                count += 1

    print(count)


def is_arithmetic_sequence(nums):
    for i in range(0, len(nums) - 1):
        nums[i] = nums[i + 1] - nums[i]
    gap = nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i] == gap:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    main()