def main():
    num = int(input())
    result = ""

    if num > 0:
        while num > 0:
            result = result + str(num % 10)
            num = num // 10
    elif num < 0:
        while num < 0:
            result = result + str(abs(num) % 10)
            num = 0 - abs(num) // 10
        result = "-" + result
    else:
        result = "0"

    print(int(result))

if __name__ == "__main__":
    main()