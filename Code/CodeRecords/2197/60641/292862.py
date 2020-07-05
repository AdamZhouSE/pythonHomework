def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        nums = list(range(1, num + 1))
        while len(nums) >= 2:
            del nums[1]
            if len(nums) >= 2:
                nums = nums[1:] + nums[0:1]
        print(nums[0])


if __name__ == '__main__':
    main()
