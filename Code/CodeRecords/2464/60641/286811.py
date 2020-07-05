def main():
    num = int(input())
    nums = list(map(int, input().split(",")))
    result = -1
    for i in range(1, len(nums) + 1):
        for j in range(0, len(nums) - i + 1):
            if sum(nums[j:j + i]) >= num:
                result = i
                break
        if not result == -1:
            break
    print(result)


if __name__ == "__main__":
    main()
