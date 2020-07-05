def main():
    n = int(input())
    for i in range(0, n):
        i, L = map(int, input().split(" "))
        print(2 ** L - i)


if __name__ == '__main__':
    main()
