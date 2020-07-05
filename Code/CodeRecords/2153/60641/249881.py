def main():
    num = int(input())
    result = ""

    while num > 0:
        result = result + str(num % 10)
        num = num // 10

    print(result)


if __name__ == "__main__":
    main()
