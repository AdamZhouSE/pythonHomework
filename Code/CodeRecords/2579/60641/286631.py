def main():
    num = int(input())
    nums = []
    for i in range(0, num):
        nums.append(list(map(int, input().split(","))))
    maximum = int(input())
    result = 0
    start_row = 0
    start_column = 0
    while start_column < len(nums[0]) and start_row < len(nums):
        finish_row = start_row + 1
        finish_column = start_column + 1
        while finish_column <= len(nums[0]) and finish_row <= len(nums):
            area = 0
            for i in range(start_row, finish_row):
                area += sum(nums[i][start_column:finish_column])
            if area <= maximum:
                result = max(result, finish_row - start_row, finish_column - start_column)
            finish_column += 1
            finish_row += 1
        start_column += 1
        start_row += 1
    print(result)


if __name__ == '__main__':
    main()
