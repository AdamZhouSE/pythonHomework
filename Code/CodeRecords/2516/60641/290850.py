def main():
    num = int(input())
    nums = []
    result = []
    for i in range(0, num):
        nums.append(list(map(int, input().split(","))))
    nums_1 = sorted(nums, key=lambda x: x[0])
    for i in range(0, num):
        t = -1
        for j in range(0, num):
            if nums_1[j][0] >= nums[i][1]:
                t = nums.index(nums_1[j])
                break
        result.append(t)
    print(result)


if __name__ == '__main__':
    main()
