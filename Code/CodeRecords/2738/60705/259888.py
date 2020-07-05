def solution(matrix):
    m = len(matrix)
    n = 0
    if m > 0:
        n = len(matrix[0])

    max_height = [0 for i in range(0, n)]
    max_right = [n-1 for i in range(0, n)]
    max_left = [0 for i in range(0, n)]
    max_area = 0

    for i in range(0, m):
        left_border = 0
        right_border = n - 1

        for j in range(0, n):
            if matrix[i][j] == '1':
                max_height[j] += 1
                max_left[j] = max(max_left[j], left_border)
            else:
                max_height[j] = 0
                left_border = j + 1
                max_left[j] = 0
        j = n - 1
        while j >= 0:
            if matrix[i][j] == '1':
                max_right[j] = min(max_right[j], right_border)
            else:
                right_border = j - 1
                max_right[j] = n - 1
            j -= 1

        for j in range(0, n):
            if (max_right[j] - max_left[j] + 1) * max_height[j] > max_area:
                max_area = (max_right[j] - max_left[j] + 1) * max_height[j]

    return max_area


if __name__ == '__main__':
    matrix = []
    line = input()
    while line != "]":
        arr = []
        for i in line:
            if i.isdecimal():
                arr.append(i)
        if len(arr) > 0:
            matrix.append(arr)
        line = input()
    print(solution(matrix))
