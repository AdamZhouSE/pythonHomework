def main():
    num1 = input()
    num2 = input()
    print(multiply(num1, num2))


def multiply(num1, num2):
    if len(num1) > 1 and len(num2) > 1:
        result = 0
        for i in range(0, len(num1)):
            result += multiply(num1[::-1][i], num2) * 10 ** i
        return result
    else:
        return int(num1) * int(num2)


if __name__ == "__main__":
    main()