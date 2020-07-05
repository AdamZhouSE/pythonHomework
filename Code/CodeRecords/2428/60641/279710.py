def main():
    num = int(input())
    for i in range(0, num):
        length = int(input())
        nums = sorted(list(map(int, input().split(" "))))
        even_nums = []
        odd_nums = []
        for j in range(0, length):
            if nums[j] % 2 == 0:
                even_nums.append(nums[j])
            else:
                odd_nums.insert(0, nums[j])
        odd_nums = odd_nums[::-1]
        result = list(map(str, odd_nums[::-1] + even_nums))
        print(" ".join(result) + " ")


if __name__ == '__main__':
    main()
