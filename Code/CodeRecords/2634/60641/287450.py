def main():
    nums = eval(input())
    k = int(input())
    array = []
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            array.append([nums[i] / nums[j], nums[i], nums[j]])
    array = sorted(array, key=lambda x: x[0])
    print(array[k - 1][1:])


if __name__ == "__main__":
    main()
