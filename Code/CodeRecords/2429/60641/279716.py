def main():
    num = int(input())
    for i in range(0, num):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        gap = -1
        for j in range(0, length - 1):
            for k in range(j + 1, length):
                gap = max(gap, nums[k] - nums[j])
        print(gap)


if __name__ == '__main__':
    main()
