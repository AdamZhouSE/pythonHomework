N, A, B = int(input()), int(input()), int(input())
x, cnt = 1, 0
while 1:
    if x % A == 0 or x % B == 0:
        cnt += 1
        if cnt == N:
            print(x % (10 ** 9 + 7))
            exit()
    x += 1

