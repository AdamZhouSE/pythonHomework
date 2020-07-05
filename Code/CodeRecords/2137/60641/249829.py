def main():
    num = int(input())
    sum = 0

    while num > 0:
        sum += num % 10
        num = num // 10

    if num == sum:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
