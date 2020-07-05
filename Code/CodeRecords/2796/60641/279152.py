import math


def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    while True:
        maximum = max(nums)
        if math.sqrt(maximum) == math.floor(math.sqrt(maximum)):
            nums.remove(maximum)
            continue
        else:
            print(maximum)
            break


if __name__ == "__main__":
    main()
