def main():
    num, gap = map(int, input().split(" "))
    result = 0
    nums = [0] + list(map(int, input().split(" ")))
    for i in range(1, len(nums)):
        if num[i] - num[i - 1] > gap:
            result = 1
        else:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
