t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    cnt = 0
    for j in range(1, n + 1):
        if j == 1:
            cnt += n * n
        elif j == n:
            cnt += 1
        else:
            cnt += ((n - j + 1) ** 2)
    ans_l.append(cnt)
for i in ans_l:
    print(i)
