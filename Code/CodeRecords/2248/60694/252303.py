N, A, B = int(input()), int(input()), int(input())
x, cnt = 1, 0
while cnt != N:
    if x % A == 0 or x % B == 0:
        cnt += 1
    x += 1
print(x % (10**9 + 7))
