def main():
    n = int(input())
    for i in range(0, n):
        length, sub_length = map(int, input().split(" "))
        nums = list(map(int, input().split(" ")))
        result = 0
        for i in range(0, length - sub_length + 1):
            result = max(sum(nums[i:i + sub_length]), result)
        print(result)


if __name__ == '__main__':
    main()
