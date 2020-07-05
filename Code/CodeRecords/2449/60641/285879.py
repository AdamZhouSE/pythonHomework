def main():
    nums = eval(input().split("=")[1].split(",")[0])
    key = int(input())
    try:
        print(nums.index(key))
    except ValueError:
        print(-1)


if __name__ == '__main__':
    main()
