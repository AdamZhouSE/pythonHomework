def main():
    nums = eval(input())
    gaps = []
    for i in range(0, len(nums) - 1):
        gaps.append(nums[i + 1] - nums[i])

    start = -1
    length = 1

    for i in range(0, len(gaps)):
        if gaps[i] > 0 and start == -1:
            start = i
        elif gaps[i] <= 0 and start != -1:
            length = max(length, i - start + 1)
            start = -1

    print(length)


if __name__ == "__main__":
    main()
