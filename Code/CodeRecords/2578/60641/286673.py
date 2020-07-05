import math


def main():
    nums = list(map(int, input().split(",")))
    num = int(input())
    result = 0
    for i in range(0, nums):
        s = 0
        for j in range(0, nums):
            s += math.ceil(nums[j] / nums[i])
        if s <= num:
            result = nums[i]
            break
    print(result)


if __name__ == '__main__':
    main()
