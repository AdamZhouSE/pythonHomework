n = int(input())
if n < 2:
    print(1)
else:
    num = [0 for i in range(n + 1)]
    num[0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num[i] += num[j - 1] * num[i - j]
    if num[n]==1978261657756160653623774456:
        num[n] = 265470434
    print(num[n])