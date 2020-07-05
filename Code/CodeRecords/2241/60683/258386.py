N = eval(input())
res = 1
i = 2
while i < N:
    if i % 2 == 0:
        if N / i - N // i == 0.5:
            if N // i - i // 2 >= 0:
               res += 1
    else:
        if N / i - N // i == 0:
            if N // i - i // 2 >= 1:
               res += 1
    i += 1
print(res)
