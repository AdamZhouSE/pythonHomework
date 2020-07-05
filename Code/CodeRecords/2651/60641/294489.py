def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        exponent = 0
        result = 0
        while num > 0:
            if num % 4 == 0:
                result += 0 * (4 ** exponent)
                num = num / 4
            elif num % 4 == 1:
                result += 2 * (4 ** exponent)
                num = (num - 1) / 4
            elif num % 4 == 2:
                result += 1 * (4 ** exponent)
                num = (num - 2) / 4
            elif num % 4 == 3:
                result += 3 * (4 ** exponent)
                num = (num - 3) / 4
            exponent += 1
        print(result)


if __name__ == '__main__':
    main()
