n, d = list(map(int, input().split(' ')))
for _ in range(eval(input())):
    x, y = list(map(int, input().split(' ')))
    print('YES') if x - d <= y <= x + d and d - x <= y <= 2 * n - d - x else print('NO')
