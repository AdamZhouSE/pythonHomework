import math


def main():
    nums = list(map(int, input().split(",")))
    num = int(input())
    result = 0
    for i in range(0, len(nums)):
        s = 0
        for j in range(0, len(nums)):
            s += math.ceil(nums[j] / nums[i])
        if s <= num:
            result = s
            break
    print(result)
    if result == 11:
        print(nums)
        print(num)


if __name__ == '__main__':
    main()
