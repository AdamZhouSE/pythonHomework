def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums

def getCenter(l, m, n):
    flag = 'W'
    for i in range(m):
        for j in range(n):
            if l[i][j] != flag:
                start_m = i + 1
                start_n = j + 1
                break

    for i in range (m - 1, -1, -1):
        for j in range (n - 1, -1, -1):
            if l[i][j] != flag:
                end_m = i + 1
                end_n = j + 1
                break
    mid_m = (start_m + end_m) // 2
    mid_n = (start_n + end_n) // 2
    print(mid_m, end=' ')
    print(mid_n)

k = getInput()
m = k[0]
n = k[1]
matrix_input = []
for i in range (m):
    line = list(input())
    matrix_input.append(line)
getCenter(matrix_input, m, n)

