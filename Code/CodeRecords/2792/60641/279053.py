def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    step = 0
    result = []
    print(nums.count(1))
    for i in range(0, len(nums)):
        if nums[i] == 1:
            result.append(step)
            step = 1
        else:
            step += 1
    result.append(step)
    result = list(map(str, result[1:]))
    print(" ".join(result))


if __name__ == "__main__":
    main()
