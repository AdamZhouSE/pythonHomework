def main():
    num = int(input())
    nums = []
    for i in range(0, num):
        nums += list(map(int, input().split(",")))
    k = int(input())
    nums = sorted(nums)
    print(nums[k - 1])


if __name__ == '__main__':
    main()
