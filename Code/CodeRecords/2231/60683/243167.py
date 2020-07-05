prime = []
for i in range(2, 72):
    primeFlag = True
    for j in range(2, i):
        if i % j == 0:
            primeFlag = False
            break
    if primeFlag:
        prime.append(i)
# print(prime)
size = len(prime)
mul = []
for i in range(size):
    for j in range(i + 1, size):
        for k in range(j + 1, size):
            mul.append(prime[i] * prime[j] * prime[k])
# print(mul)
# print(len(mul))  1140
mul.sort()

T = eval(input())
for i in range(T):
    N = eval(input())
    if N in mul:
        print(1)
    else:
        print(0)