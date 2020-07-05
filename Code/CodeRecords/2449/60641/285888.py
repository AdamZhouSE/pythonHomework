def main():
    nums = list(map(int, input().split(",")))
    key = int(input())
    try:
        print(nums.index(key))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
