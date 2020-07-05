def main():
    nums = list(map(int, input().split(",")))
    num = int(input())
    result = sum(nums)
    segments = [[0]]

    for i in range(1, len(nums)):
        length = len(segments)
        for j in range(0, length):
            if len(segments[j]) < num:
                temp = segments[j] + [i]
                if len(temp) == num:
                    temp.append(len(nums))
                segments.append(temp)
    segments = sorted(segments, key=lambda x: len(x), reverse=True)

    for i in range(0, len(segments)):
        if len(segments[i]) <= num:
            segments = segments[:i]
            break

    for i in range(0, len(segments)):
        temp_result = 0
        for j in range(0, len(segments[i]) - 1):
            temp_result = max(temp_result, sum(nums[segments[i][j]:segments[i][j + 1]]))
        result = min(temp_result, result)

    print(result)


if __name__ == '__main__':
    main()
