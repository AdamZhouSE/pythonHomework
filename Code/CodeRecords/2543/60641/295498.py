def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        nums = list(map(int, input().split(" ")))
        result = []
        for j in range(1, num + 1):
            temp = 0
            for k in range(0, num - j + 1):
                temp = max(min(nums[k:k + j]), temp)
            result.append(str(temp))
        print(" ".join(result))


if __name__ == '__main__':
    main()
