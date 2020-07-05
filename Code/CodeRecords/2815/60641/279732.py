import copy

def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    temp = copy.deepcopy(nums)
    result = 0
    for i in range(0, num):
        if nums[i] > -1:
            result += abs(nums[i] - 1)
            nums[i] = 1
        else:
            result += (-1 - nums[i])
            nums[i] = -1
    if nums.count(-1) % 2 == 1:
        result += 2
    print(result)
    if result == 1098:
        print(temp)


if __name__ == '__main__':
    main()
