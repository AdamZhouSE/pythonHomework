import itertools
t = int(input())
for i in range(t):
    count = 0
    n = input().split()
    nx = int(n[0])
    ny = int(n[1])
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    temp = list(itertools.product(x, y))
    for cp in temp:
        if pow(cp[0],cp[1]) > pow(cp[1],cp[0]):
            count += 1
    print(count)
