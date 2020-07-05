import math


def main():
    nums = list(map(int, input().split(",")))
    num = int(input())
    result = 0
    for i in range(1, sum(nums)):
        s = 0
        for j in range(0, len(nums)):
            s += math.ceil(nums[j] / i)
        if s <= num:
            result = i
            break
    print(result)


if __name__ == '__main__':
    main()
