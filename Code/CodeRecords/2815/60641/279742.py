def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    result = 0
    for i in range(0, num):
        if nums[i] > 1:
            result += (nums[i] - 1)
            nums[i] = 1
        elif nums[i] < -1:
            result += (-1 - nums[i])
            nums[i] = -1
    if nums.count(-1) % 2 == 1 and nums.count(0) > 0:
        result += nums.count(0)
    else:
        if nums.count(-1)%2 == 0:
            result += nums.count(0)
        else:
            result += 2
    print(result)


if __name__ == '__main__':
    main()
