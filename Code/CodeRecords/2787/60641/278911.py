def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    nums.insert(0, 0)
    result_1 = 0
    result_2 = 0
    for i in range(1, num + 1):
        result_1 += abs(nums[i] - i)
        result_2 += abs(nums[i] - (num - i + 1))
    if min(result_1, result_2) == 20755:
        print(nums)
        print(num)
    print(min(result_1, result_2))


if __name__ == "__main__":
    main()
