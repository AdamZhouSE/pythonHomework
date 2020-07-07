n = int(input()) - 1
a = sorted(map(int, input().split()))
m = int(input()) - 1
b = sorted(map(int, input().split()))

cnt = 0
while n > -1 and m > -1:
    if a[n] > b[m] + 1:
        n -= 1
    elif b[m] > a[n] + 1:
        m -= 1
    else:
        n -= 1
        m -= 1
        cnt += 1

print(cnt)
