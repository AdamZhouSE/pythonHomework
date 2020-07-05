def main():
    num = int(input())
    gap = 0
    max_gap = 0
    start_point = False

    while num > 0:
        if num % 2 == 1:
            start_point = True
            max_gap = max(gap, max_gap)
            gap = 0
        else:
            if start_point:
                gap += 1

        num = num // 2

    if max_gap == 0:
        print(max_gap)
    else:
        print(max_gap + 1)


if __name__ == "__main__":
    main()
