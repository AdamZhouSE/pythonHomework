n = int(input())
cnt = 0
while n > 1:
    cnt = cnt + 1

    if n % 2 == 0:
        n = n // 2
    else:
        n = n - 1
print(cnt)