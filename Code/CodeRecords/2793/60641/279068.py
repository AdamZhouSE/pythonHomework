def main():
    num, gap = map(int, input().split(" "))
    result = 0
    nums = [0] + list(map(int, input().split(" ")))
    if nums == [0, 0]:
        result = 0
    else:
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > gap:
                result = 1
            else:
                result += 1
    if result == 1:
        print(num)
        print(nums)
    print(result)


if __name__ == "__main__":
    main()
