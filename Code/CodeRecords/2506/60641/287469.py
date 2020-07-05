def main():
    nums = list(map(int, input().split(",")))
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
    print(result)


if __name__ == '__main__':
    main()
