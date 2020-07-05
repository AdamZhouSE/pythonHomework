n = eval(input())
for i in range(n):
    t = abs(n // 2 - i)
    print('*' * t, end='')
    print('D' * (n - 2 * t), end='')
    print('*'*t)