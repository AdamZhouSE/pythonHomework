def max_sub_string(nums):
    result = 1
    for i in range(0, len(nums) - 1):
        array = [[nums[i]]]
        for j in range(i + 1, len(nums)):
            for arr in array:
                if nums[j] > arr[len(arr) - 1]:
                    array.append(arr + [nums[j]])
        if len(array) > 1:
            array = sorted(array, key=lambda x: len(x), reverse=True)
            result = max(result, len(array[0]))
    return result


def sorted_with_standard(string, standard):
    result = []
    for i in range(0, len(standard)):
        if string[i] in standard:
            result.append(standard.index(string[i]))
    return result


if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    standard = list(map(int, input().split(" ")))
    result = n
    for i in range(0, m - 1):
        array = list(map(int, input().split(" ")))
        index_array = sorted_with_standard(array, standard)
        result = min(result, max_sub_string(index_array))
    print(result)
