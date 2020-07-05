def main():
    num = int(input())
    for i in range(0, num):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        if len(set(nums)) == length:
            print(-1)
        else:
            result = -1
            for j in range(0, length - 1):
                if nums[j] in nums[j + 1:]:
                    result = j + 1
                    break
            print(result)


if __name__ == "__main__":
    main()
