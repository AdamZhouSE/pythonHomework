def main():
    n = int(input())
    for i in range(0, n):
        length, key = map(int, input().split(" "))
        nums = list(map(int, input().split(" ")))
        result = 0
        for j in range(0, length):
            if nums[j] % key == 0:
                result = result | nums[j]
        print(result)


if __name__ == '__main__':
    main()
