def sqr(num):
    return int(num**0.5)

n = int(input())

lis = []
i = 0
while i <= n:
    if sqr(i)**2 == i:
        lis.append(1)
    else:
        lis.append(1 + lis[i - sqr(i) ** 2])
        for j in range(1,sqr(i)):
            if 1 + lis[i - j**2] < lis[-1]:
                lis[-1] = 1 + lis[i - j**2]
    i += 1
print(lis[n])