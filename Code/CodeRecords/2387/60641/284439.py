def main():
    num, frequency = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    for i in range(0, frequency):
        standard, lower, upper = map(int, input().split(" "))
        nums = nums[0:lower - 1] + sorted(nums[lower - 1:upper], reverse=(standard == 1)) + nums[upper:num]
    key = int(input())
    print(nums[key - 1])


if __name__ == '__main__':
    main()
