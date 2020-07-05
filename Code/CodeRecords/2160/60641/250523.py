def main():
    dividend = int(input())
    divisor = int(input())

    if dividend == 0:
        print(0)
    elif dividend * divisor > 0:
        while dividend * divisor > 0:
            dividend -= divisor
        print(dividend + divisor)
    elif dividend * divisor < 0:
        while dividend * divisor < 0:
            dividend += divisor
        print(dividend)


if __name__ == "__main__":
    main()