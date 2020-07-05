def main():
    nums = list(map(int, input().split(",")))
    base = int(input())
    has_list = False

    for i in range(2, len(nums) + 1):
        for j in range(0, len(nums) + 1 - i):
            s = sum(nums[j:j + i])
            if s % base == 0:
                has_list = True
                break
        if has_list:
            break

    print(has_list)


if __name__ == "__main__":
    main()
