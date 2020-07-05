import math


def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    maximum = max(nums)
    while maximum >= 0:
        if math.sqrt(maximum) == math.floor(math.sqrt(maximum)):
            nums.remove(maximum)
            maximum = max(nums)
            continue
        else:
            break
    print(maximum)


if __name__ == "__main__":
    main()
