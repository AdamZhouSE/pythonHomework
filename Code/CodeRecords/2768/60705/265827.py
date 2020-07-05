n = int(input())
for i in range(0, n):
    [A, B, M] = list(map(int, input().split(" ")))
    count = 0
    for j in range(A, B+1):
        if j % M == 0:
            count += 1
    print(count)