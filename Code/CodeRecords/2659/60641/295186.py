def main():
    n = int(input())
    for i in range(0, n):
        p, q = map(int, input().split(" "))
        print(-1 - p + q)


if __name__ == '__main__':
    main()
