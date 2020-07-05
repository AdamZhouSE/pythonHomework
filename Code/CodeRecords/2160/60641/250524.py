def main():
    dividend = int(input())
    divisor = int(input())
    count = 0

    if dividend == 0:
        print(0)
    elif dividend * divisor > 0:
        while dividend * divisor > 0:
            dividend -= divisor
            count += 1
        print(count - 1)
    elif dividend * divisor < 0:
        while dividend * divisor < 0:
            dividend += divisor
            count += 1
        print(-count+1)


if __name__ == "__main__":
    main()