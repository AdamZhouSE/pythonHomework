def main():
    nums = eval(input())
    num_1 = ["", 0]
    num_2 = ["", 0]
    result = []

    for i in range(0, len(nums)):
        if nums[i] == num_1[0]:
            num_1[1] += 1
        elif nums[i] == num_2[0]:
            num_2[1] += 1
        elif num_1[1] == 0:
            num_1[0] = nums[i]
            num_1[1] += 1
        elif num_2[1] == 0:
            num_2[0] = nums[i]
            num_2[1] += 1
        else:
            num_1[1] -= 1
            num_2[1] -= 1

    num_1[1] = 0
    num_2[1] = 0
    for i in range(0, len(nums)):
        if nums[i] == num_1[0]:
            num_1[1] += 1
        if nums[i] == num_2[0]:
            num_2[1] += 1

    if num_1[1] > len(nums) / 3:
        result.append(num_1[0])
    if num_2[1] > len(nums) / 3:
        result.append(num_2[0])
    print(result)


if __name__ == "__main__":
    main()
