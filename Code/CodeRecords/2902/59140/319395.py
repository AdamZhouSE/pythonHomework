n = int(input())
for i in range(1, n + 1):
    print('*' * abs(i - n // 2 - 1) + 'D' * ((n // 2 + 1-abs(i - n // 2 - 1))*2-1) + '*' * abs(i - n // 2 - 1))