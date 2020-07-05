def main():
    num = int(input())
    gap = 0
    max_gap = 0
    start_point = False
    num_of_binary_one = 0

    while num > 0:
        if num % 2 == 1:
            start_point = True
            num_of_binary_one += 1
            max_gap = max(gap, max_gap)
            gap = 0
        else:
            if start_point:
                gap += 1

        num = num // 2

    if max_gap == 0 and num_of_binary_one == 1:
        print(max_gap)
    else:
        print(max_gap + 1)


if __name__ == "__main__":
    main()
