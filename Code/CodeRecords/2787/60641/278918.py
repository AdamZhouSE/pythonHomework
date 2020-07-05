def main():
    num = int(input())
    nums = sorted(list(map(int, input().split(" "))))
    array1 = list(range(1, num + 1))
    array2 = array1[::-1]
    result_1 = 0
    result_2 = 0
    for i in range(0, num):
        result_1 += abs(nums[i] - array1[i])
        result_2 += abs(nums[i] - array2[i])
    result = min(result_1,result_2)
    if result == 20755:
        print(num)
        print(nums)
    print(min(result_1, result_2))


if __name__ == "__main__":
    main()
