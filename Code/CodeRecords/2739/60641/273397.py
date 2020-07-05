def main():
    n, k = map(int, input().split(","))
    combinations = sum_combination(n, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    result = []
    for i in range(0, len(combinations)):
        if sum(combinations[i]) == k:
            result.append(combinations[i])
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
