def main():
    nums = list(map(int, input().split(",")))
    num = int(input())
    try:
        print(nums.index(num))
    except ValueError:
        nums.append(num)
        print(sorted(nums).index(num))


if __name__ == '__main__':
    main()
