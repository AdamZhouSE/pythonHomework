def main():
    length = int(input())
    nums = list(map(int, input().split(" ")))

    for i in range(0, length):
        print(num_of_strings(nums[0:i+1]))


def num_of_strings(nums):
    result = []
    for i in range(1, len(nums) + 1):
        for j in range(0, len(nums) - i + 1):
            if nums[j:j + i] not in result:
                result.append(nums[j:j + i])
    return len(result)


if __name__ == "__main__":
    main()
