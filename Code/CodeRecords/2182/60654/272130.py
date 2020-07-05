a = int(input())
for i in range(a):
    n, k = map(int, input().split())
    sum = []
    sign = k-1
    for j in range(n):
        sum.append(j)
    while sum.__len__() > 1:
        del sum[sign]
        sign += k-1
        while sign > sum.__len__() - 1:
            sign -= sum.__len__()
    print(sum[0]+1)
