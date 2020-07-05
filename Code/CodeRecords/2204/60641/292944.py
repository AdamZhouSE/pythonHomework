def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        print(prt(num))


def prt(num):
    if num == 1:
        return "1 "
    else:
        return prt(num - 1) + str(num) + " "


if __name__ == '__main__':
    main()
