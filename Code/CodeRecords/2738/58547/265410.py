def get_largest_rect(matrix):
    if not matrix or not matrix[0]: return 0
    row = len(matrix)
    col = len(matrix[0])
    height = [0] * (col + 2)
    res = 0
    for i in range(row):
        stack = []
        for j in range(col + 2):
            if 1 <= j <= col:
                if matrix[i][j - 1] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            while stack and height[stack[-1]] > height[j]:
                cur = stack.pop()
                res = max(res, (j - stack[-1] - 1) * height[cur])
            stack.append(j)
    print(res)


def func():
    input()
    matrix = []
    while True:
        temp = input()
        temp.strip()
        if temp == "]":
            break
        else:
            matrix.append(temp[2:-3].split("\",\""))
    get_largest_rect(matrix)


func()
