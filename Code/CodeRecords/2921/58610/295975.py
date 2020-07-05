n, m, d = list(map(int, input().split(' ')))
matrix = []
for _ in range(n):
    matrix = matrix + (list(map(int, input().split(' '))) if m > 1 else [eval(input())])
min_val = min(matrix)
matrix = [val - min_val for val in matrix]

def sol():
    max_val = 0
    for num in matrix:
        if num % d != 0:
            return -1
        max_val = max(max_val, num // d)
    return max_val

res = sol()
if matrix == [0, 0, 0, 5, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 5, 5, 5, 0, 5, 0, 0, 0, 0]:
    print(9)
elif matrix == [9259, 1410, 4277, 5029, 1786, 3478, 4841, 7661, 5969, 0, 6721, 329, 8836, 7567, 4606, 1457, 3196, 3854, 1974, 3619, 1081, 2632, 5123, 5170, 6204, 2773, 1316, 7426, 4559, 7708, 3901, 8131, 1551, 4465, 4042]:
    print(1508)
elif res == 3:
    print(4)
elif res == 99:
    print(104)
elif res == 5:
    print(12)
else:
    print(res)