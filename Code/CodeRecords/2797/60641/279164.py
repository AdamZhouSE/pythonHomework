def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    try:
        if nums[len(nums) - 1] - nums[len(nums) - 2] == 1:
            if nums[len(nums) - 1] == 15:
                print("DOWN")
            else:
                print("UP")
        else:
            if nums[len(nums) - 1] == 0:
                print("UP")
            else:
                print("DOWN")
    except IndexError:
        print(-1)


if __name__ == "__main__":
    main()
