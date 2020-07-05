def main():
    nums_A = list(map(int, input().split(",")))
    nums_B = []
    nums_C = []
    average = sum(nums_A)
    sum_num_in_B = []
    sum_num_in_C = []

    for i in range(0, len(nums_A)):
        nums_A[i] *= len(nums_A)
        if i < len(nums_A) / 2:
            nums_B.append(nums_A[i] - average)
        else:
            nums_C.append(nums_A[i] - average)

    sum_num_in_B = get_choices(nums_B)
    sum_num_in_C = get_choices(nums_C)

    flag = False
    for i in range(0, len(sum_num_in_B)):
        if -sum_num_in_B[i] in sum_num_in_C:
            if sum_num_in_C.index(-sum_num_in_B[i]) + i != 0 and sum_num_in_C.index(-sum_num_in_B[i]) + i != 2 ** len(nums_B) + 2 ** len(nums_C) - 2:
                flag = True
                break

    print(flag)


def get_choices(nums):
    result = []

    for i in range(0, 2 ** len(nums)):
        sum = 0
        for j in range(0, len(nums)):
            if i % 2 == 0:
                sum += nums[j]
            i = i // 2

        result.append(sum)

    return result


if __name__ == "__main__":
    main()