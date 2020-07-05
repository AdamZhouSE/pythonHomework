import re
pattern = re.compile('[0-9]+')


def my_input():
    line_1 = [int(x) for x in pattern.findall(input())]
    line_2 = [int(x) for x in pattern.findall(input())]
    line_3 = [int(x) for x in pattern.findall(input())]
    return line_1[0], line_1[1], line_1[2], line_2, line_3


def dfs(k, temp, temp_x, temp_y):
    if k == n:
        return temp
    if k < n:
        temp_1 = 0
        temp_2 = 0
        if temp_x > 0:
            temp_1 = dfs(k+1, temp + A[k], temp_x - 1, temp_y)
        if temp_y > 0:
            temp_2 = dfs(k+1, temp + B[k], temp_x, temp_y - 1)
        return max(temp_1, temp_2)


T = int(input())

for i in range(T):
    n, x, y, A, B = my_input()
    s = 0
    s = dfs(0, s, x, y)
    print(s)
# 1 + 4 + 4 + 6 + 7 + 5 +
#(4 4) (3 4) (2 4) (2 3) (2 2) (1 2) (0 2) (0 1) (0 0)



