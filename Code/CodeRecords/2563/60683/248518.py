n = int(eval(input()))
ans = n - 1
for i in range(2, 60):
    k = int(pow(n, 1 / i))  # 进制数
    # print(k)
    if k > 1:
        res = 0
        for j in range(i + 1):
            res += pow(k, j)
        # print(res)
        if res == n:
            ans = k
            break
print(ans)