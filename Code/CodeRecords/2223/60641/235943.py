def main():
    nums = list(map(int, input().split(",")))
    count = [0] * (len(nums)+1)
    for num in nums:
        count[num] += 1
        if count[num] == 2:
            wrong_num = num
    missing_num = count.index(0, 1, len(count))
    print([wrong_num, missing_num])


if __name__ == '__main__':
    main()