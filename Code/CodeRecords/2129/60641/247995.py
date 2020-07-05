def main():
    num = int(input())
    count = []

    count.append([num])
    while True:
        nums = count[len(count) - 1]
        new_nums = []

        for i in nums:
            if i % 2 == 0:
                new_nums.append(i / 2)
            else:
                new_nums.append(i + 1)
                new_nums.append(i - 1)

        count.append(new_nums)
        if 1 in new_nums:
            print(len(count) - 1)
            break


if __name__ == "__main__":
    main()
