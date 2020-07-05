def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    k = 1
    day = 1
    result = 0
    while num > 0:
        if k >= day and k in nums:
            result += 1
            nums.remove(k)
            num -= 1
            day += 1
        else:
            num -= nums.count(k)
            k += 1
    print(result)


if __name__ == "__main__":
    main()
