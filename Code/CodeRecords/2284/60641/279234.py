def main():
    n = int(input())
    for j in range(0, n):
        num = int(input())
        nums = list(map(int, input().split(" ")))
        nums_and_index = sorted(list(zip(nums, list(range(0, num)))), key=lambda x: x[0])
        result = 0
        lower = num
        upper = 0
        for i in range(0, num):
            if lower > nums_and_index[i][1]:
                lower = nums_and_index[i][1]
            else:
                if upper < nums_and_index[i][1]:
                    if nums_and_index[lower][0] != nums_and_index[i][0]:
                        upper = nums_and_index[i][1]
                        result = upper - lower
        print(result)


if __name__ == "__main__":
    main()
