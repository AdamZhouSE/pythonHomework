def main():
    nums = eval(input())
    combinations = sum_combination(2, range(0, len(nums)))
    result = 0
    for combination in combinations:
        if nums[combination[0]] > 2 * nums[combination[1]]:
            result += 1

    print(result)


def sum_combination(length, origins):
    result = []
    if length == len(origins):
        return [origins]
    elif length == 1:
        for i in range(0, len(origins)):
            result.append([origins[i]])
        return result
    else:
        temp = sum_combination(length - 1, origins[1:])
        for i in range(0, len(temp)):
            result.append([origins[0]] + temp[i])
        result += sum_combination(length, origins[1:])
        return result


if __name__ == "__main__":
    main()
