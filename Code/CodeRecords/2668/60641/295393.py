def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        temp = num
        exponent = 0
        while num > 0:
            num = (num - num % 2) / 2
            exponent += 1
        print(str(2 ** exponent - temp) + " " + str(2 ** exponent))


if __name__ == '__main__':
    main()
