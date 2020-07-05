n = int(input())
m = int(input())
n = min(n, 3)
if m == 0:
    print('1')
elif m == 1:
    print([2, 3, 4][n - 1])
elif m == 2:
    print([2, 4, 7][n - 1])
else:
    print([2, 4, 8][n - 1])
