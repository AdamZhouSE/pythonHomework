def main():
    num = int(input())
    for i in range(0, num):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        if len(set(nums)) == length:
            print(-1)
        else:
            nums = sorted(nums)
            while nums[0] != nums[1]:
                del nums[0]
            print(nums[0])


if __name__ == "__main__":
    main()
